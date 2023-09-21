#!/usr/bin/python

__author__ =  'vikram(vikramprasad249@gmail.com)'
__version__=  '0.1'
__modified_by = 'vikram'

class Service:
    extrainfo = ''
    name = ''
    product = ''
    fingerprint = ''
    version = ''

    def __init__( self, ServiceNode ):
        self.extrainfo = ServiceNode.getAttribute('extrainfo')
        self.name = ServiceNode.getAttribute('name')
        self.product = ServiceNode.getAttribute('product')
        self.fingerprint = ServiceNode.getAttribute('servicefp')
        self.version = ServiceNode.getAttribute('version')
