#!/usr/bin/env python

### IMPORTS ###
import uuid

from celery import Celery

### GLOBALS ###

### FUNCTIONS ###
def makeCelery( app):
    celery = Celery( app.import_name, broker = app.config[ 'CELERY_BROKER_URL'])
    celery.conf.update( app.config)
    TaskBase = celery.Task
    class ContextTask( TaskBase):
        abstract = True
        def __call__( self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__( self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

@celery.task()
def add_together( a, b):
    return a + b

### CLASSES ###

### MAIN ###
if __name__ == '__main__':
    pass
