#!/usr/bin/env python

### IMPORTS ###
from celery import task

### GLOBALS ###

### FUNCTIONS ###
@task( bind = True)
def add_together( self, a, b):
    print "Result: %d" % ( int( a + b), )
    return a + b

### CLASSES ###
#class CeleryMath:
#    def __init__( self, celery):
#        self.celery = celery

### MAIN ###
if __name__ == '__main__':
    pass
