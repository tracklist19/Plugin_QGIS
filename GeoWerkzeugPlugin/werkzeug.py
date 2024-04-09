from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from GeoWerkzeugPlugin.werkzeug_funktionalitaet import *

import os


class GeoWerkzeug:

    def __init__ (self, iface):
        self.iface = iface

    def initGui(self):

        # Pfad zum Plugin/aktuelle Datei (relativer Pfad)
        pluginPath = os.path.dirname(__file__)
        # Pfad zum Icon
        iconPfad = os.path.join(pluginPath, 'Icon/index.png')

        self.startButton = QAction(QIcon(iconPfad), 'Starten', self.iface.mainWindow())
        self.iface.addPluginToMenu('GeoWerkzeug', self.startButton)
        self.iface.addToolBarIcon(self.startButton)
        # Methode maskeAufrufen aufrufen -> GUI angezeigen
        self.startButton.triggered.connect(self.maskeAufrufen)

    def unload(self):
        self.iface.removePluginMenu('GeoWerkzeug', self.startButton)

    def maskeAufrufen(self):
        self.gui = MaskeUndFunktionalitaet(self.iface.mainWindow())     # Verknuepfung mit QGIS-Fenster
        self.gui.show()


