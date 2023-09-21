#!/usr/bin/python

__author__ =  'vikram'
__version__=  '0.1'
__modified_by = 'vikram'

class Script:
    scriptId = ''
    output = ''

    def __init__( self, ScriptNode ):
        if not (ScriptNode is None):
            self.scriptId = ScriptNode.getAttribute('id')
            self.output = ScriptNode.getAttribute('output')
