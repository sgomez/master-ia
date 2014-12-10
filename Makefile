all: resources.py views/mainWindow.py

clean:
	rm -f resources.py views/mainWindow.py

resources.py: resources/config/resources.qrc
	pyrcc4 -o resources.py resources/config/resources.qrc

views/mainWindow.py: resources/views/mainWindow.ui
	pyuic4 -o views/mainWindow.py resources/views/mainWindow.ui