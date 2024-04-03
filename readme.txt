Plugin_QGIS : 
a Plugin in Python OOP for the geographic information system (GIS) software application QGIS

- Beschreibung : Dieses Plugin erstellt ausgehend von zwei Input-Files zwei Puffer-Layer, 
		 fügt beide zusammen (merge) und löst das Ergebnis optional auf
- Ordner 'GeoWerkzeugPlugin' ablegen unter : 
  C:\Users\user\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins
	(README.md & GUI-preview_GeoWerkzeug_plugin.PNG sind optional) 
  und in QGIS unter Erweiterungen aktivieren 

- werkzeug.py : fährt das Plugin hoch/herunter, ruft die GUI auf ; 
  werkzeug_funktionalitaet.py : die eigentliche Funktionalität (GUI von Datei laden, Puffer, Merge, Dissolve, usw.) 

- GUI mit Qt Designer, PyQt
- QGIS-Version: 3.10.4-A Coruña
- Python-Version: 3.7
