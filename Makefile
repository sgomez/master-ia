all: views/resources.py views/mainWindow.py

clean:
	rm -f views/resources.py views/mainWindow.py

views/resources.py: resources/config/resources.qrc
	pyrcc5 -o views/resources.py resources/config/resources.qrc

views/mainWindow.py: resources/views/mainWindow.ui
	pyuic5 -o views/mainWindow.py resources/views/mainWindow.ui
