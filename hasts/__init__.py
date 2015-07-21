#!/usr/bin/env python

### IMPORTS ###
import uuid

from flask import Flask
from flask import abort, render_template, url_for

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

@app.route( '/devices/<device_uuid>')
def showDevice( device_uuid):
    """Display information about a device in the system."""
    deviceUUID = None
    try:
        deviceUUID = uuid.UUID( device_uuid)
    except Exception as ex:
        print ex
        abort( 404)
    return 'Device %s.' % ( str( deviceUUID), )

@app.route( '/rooms/')
def showRooms():
    """Display a list of rooms."""
    return 'Room list'

@app.route( '/rooms/<room_uuid>')
def showRoom( room_uuid):
    """Display information about a room in the system."""
    roomUUID = None
    try:
        roomUUID = uuid.UUID( room_uuid)
    except Exception as ex:
        print ex
        abort( 404)
    return 'Room %s.' % ( str( roomUUID), )

### CLASSES ###

### MAIN ###
if __name__ == '__main__':
    pass

