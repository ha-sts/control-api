#!/usr/bin/env python

### IMPORTS ###
from flask import Flask

### GLOBALS ###
app = Flask( __name__)

### FUNCTIONS ###
@app.route( '/')
def hello_world():
    return 'Hello World!'

### CLASSES ###

### MAIN ###
if __name__ == '__main__':
    pass

