#!/usr/bin/env python

### IMPORTS ###
from flask import Flask

### GLOBALS ###
app = Flask( __name__)

### FUNCTIONS ###
@app.route( '/')
def helloWorld():
    """Display the index page.  This will eventually load a webapp that will access the APIs."""
    return 'Hello World!'

@app.route( '/devices/')
def showDevices():
    """Display a list of devices."""
    return 'Device list'

@app.route( '/devices/<device_id>')
def showDevice( device_id):
    """Display information about a device in the system."""
    return 'Device %d.' % ( device_id, )

@app.route( '/rooms/')
def showRooms():
    """Display a list of rooms."""
    return 'Room list'

@app.route( '/rooms/<room_id>')
def showRoom( room_id):
    """Display information about a room in the system."""
    return 'Room %d.' % ( room_id, )

### CLASSES ###

### MAIN ###
if __name__ == '__main__':
    pass

