#!/usr/bin/env python

### IMPORTS ###
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

### CLASSES ###
class CeleryMath:
    def __init__( self, celery):
        self.celery = celery
    
    def add_together

### MAIN ###
if __name__ == '__main__':
    pass
