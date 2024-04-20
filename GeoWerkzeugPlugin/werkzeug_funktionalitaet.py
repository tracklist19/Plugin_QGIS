from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5 import uic
import os
from qgis.core import *
import processing                                                               # GeoVerabeitung


# Pfad zur .ui-Datei
pluginPath = os.path.dirname(__file__)
pathUi = os.path.join(pluginPath, 'geowerkzeug.ui')

WIDGET, BASE = uic.loadUiType(pathUi)                                           # um GUI der MUF-Klasse zu uebergeben -> WIDGET: Klasse die die GUI enthält ; BASE: von Qt benötigte Generelle Klassen


class MaskeUndFunktionalitaet(WIDGET, BASE):              	                  # Klasse erbt Klassen WIDGET, BASE

    def __init__(self, parent):                           	                  # bei Instanziierung: QGIS-mainWindow wird dem Parameter parent übergeben -> innerhalb dessen wird dann Plugin-GUI angezeigt
        QDialog.__init__(self, parent)
        self.setupUi(self)                                                      # setupUi weist der Klasse alle objectNames der GUI zu -> GUI-Definitionen werden ansprechbar

        # Buttons mit Methoden verknuepfen
        self.btn_cancel.clicked.connect(self.closePlugin)
        self.btn_inputFile1.clicked.connect(self.getPathFile1)
        self.btn_inputFile2.clicked.connect(self.getPathFile2)
        self.btn_output.clicked.connect(self.getOutputPath)
        self.btn_run.clicked.connect(self.runGeoprocessing)


    def closePlugin(self):
        self.close()

    def getPathFile1(self):
        pathTuple = QFileDialog.getOpenFileName(None, 'Datensatz 1 laden', '*.shp')
        path = pathTuple[0]
        # LineEdit mit Eingabe-Pfad1 befüllen
        self.txt_inputFile1.setText(path)

    def getPathFile2(self):
        pathTuple = QFileDialog.getOpenFileName(None, 'Datensatz 2 laden', '*.shp')
        path = pathTuple[0]
        # LineEdit mit Eingabe-Pfad2 befüllen
        self.txt_inputFile2.setText(path)

    def getOutputPath(self):
        path = QFileDialog.getExistingDirectory(None, 'Output')
        self.txt_output.setText(path)

    def runGeoprocessing(self):

        # Pfade auslesen
        pathFile1 = self.txt_inputFile1.text()
        pathFile2 = self.txt_inputFile2.text()
        pathOutput = self.txt_output.text()

        # Distanzen auslesen
        distance1 = self.txt_inputDistance1.text()
        distance2 = self.txt_inputDistance2.text()

        # Output vorbereiten
        pathOutputBuffer1 = os.path.join(pathOutput, 'buffer1.shp')
        pathOutputBuffer2 = os.path.join(pathOutput, 'buffer2.shp')


        # Puffer1
        parameter1 = {

                'INPUT' : pathFile1,
                'DISTANCE' : distance1,
                'SEGMENTS' : 10,
                'DISSOLVE' : False,
                'OUTPUT' : pathOutputBuffer1
        }


        # Puffer2
        parameter2 = {

                'INPUT' : pathFile2,
                'DISTANCE' : distance2,
                'SEGMENTS' : 10,
                'DISSOLVE' : False,
                'OUTPUT' : pathOutputBuffer2
        }



        # PufferWerkzeug ausführen
        processing.run('native:buffer', parameter1)
        processing.run('native:buffer', parameter2)


        # Merge vorbereiten
        outputPathMerge = os.path.join(pathOutput, 'merge.shp')

        parameterMerge = {											        # Parameter aus der Konsolen-Hilfe

                'LAYERS': [pathOutputBuffer1, pathOutputBuffer2],
                'OUTPUT': outputPathMerge
            }

           # Merge durchfuehren 
        processing.run('native:mergevectorlayers', parameterMerge)


        if self.cb_dissolve.isChecked():

            # Dissolve
            outputPathDissolve = os.path.join(pathOutput, 'final_mit_dissolve.shp')

            parameterDissolve = {

                    'INPUT': outputPathMerge,
                    'OUTPUT': outputPathDissolve

                }

            processing.run('native:dissolve', parameterDissolve)

            layer = QgsVectorLayer(outputPathDissolve, 'Final_Dissolve', 'ogr')
            QgsProject.instance().addMapLayer(layer)


        else:
            layer = QgsVectorLayer(outputPathMerge, 'Final_ohne_Dissolve', 'ogr')
            QgsProject.instance().addMapLayer(layer)
