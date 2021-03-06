#!/usr/bin/env python

### IMPORTS ###
import uuid

from celerytasks import *

from flask import Flask
from flask import abort, render_template, url_for

### GLOBALS ###
app = Flask( __name__)

# This needs to be handled in a better way
rmqHost = 'localhost'
rmqUser = 'guest'
rmqPass = 'guest'
rmqPort = '5672'
rmqBrokerURL = 'amqp://%s:%s@%s:%s//' % ( rmqUser, rmqPass, rmqHost, rmqPort)
app.config.update( CELERY_BROKER_URL = rmqBrokerURL,
                   #CELERY_RESULT_BACKEND = rmqBrokerURL,
                   CELERY_IGNORE_RESULT = True)
celery = celerytasks.makeCelery( app)

### FUNCTIONS ###
#@celery.task()
#def add_together( a, b):
#    print "Result: %d" % ( int( a + b), )
#    return a + b

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
    return "Device %s." % ( str( deviceUUID), )

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
    return "Room %s." % ( str( roomUUID), )

@app.route( '/testcelery')
def testCelery():
    result = celerytasks.add_together.delay( 23, 37)
    return "Job submitted."

### CLASSES ###

### MAIN ###
if __name__ == '__main__':
    pass
