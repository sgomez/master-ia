all: appResources.py views/mainWindow.py

appResources.py: appResources.qrc
	pyrcc4 -o appResources.py appResources.qrc

views/mainWindow.py: views/mainWindow.ui
	pyuic4 -o views/mainWindow.py views/mainWindow.ui