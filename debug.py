#!/usr/bin/env python

### IMPORTS ###
from hasts import app

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###

### MAIN ###
def main():
    app.run( debug = True, host = '0.0.0.0', port = 8080, threaded = True)

if __name__ == '__main__':
    main()

