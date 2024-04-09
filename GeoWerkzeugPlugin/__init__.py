from GeoWerkzeugPlugin.werkzeug import *


def classFactory(iface):				 # Methode der init stellt iface (von QGIS) als Attribut der Klasse GeoWerkzeug in werkzeug.py bereit 
    return GeoWerkzeug(iface)                    # Instanz der Klasse wird erstellt, return gibt sie zurueck an QGIS -> QGIS platziert dann Plugin
