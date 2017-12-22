#!/usr/bin/env python

### IMPORTS ###
from celery import Task, task

from cassandra.cluster import Cluster

### GLOBALS ###

### FUNCTIONS ###
@task( base = CassandraTask)
def insertHealthReport( self, data):
    print "Data: %s" % ( str( data), )
    return True

### CLASSES ###
class CassandraTask( Task):
    abstract = True
    _db = None
    
    @property
    def db( self):
        if self._db is None:
            # Connect to the Cassandra database
            pass
        return self._db

### MAIN ###
if __name__ == '__main__':
    pass
