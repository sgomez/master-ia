#!/usr/bin/env python
__author__ = 'sergio'

class Container():

    _instance = None
    services = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Container, cls).__new__(cls, args, kwargs)
        return cls._instance

    def get(self, name):
        return self.services[name]

    def set(self, name, service):
        self.services[name] = service