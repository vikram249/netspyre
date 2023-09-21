#!/usr/bin/env python

'''
NetSpyre - A GUI-Based Multi-Tool for Penetration Testing with Automated Network Discovery and Analysis 

Copyright © (Vikram Prasad)
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.ext.declarative import declarative_base
from PyQt5.QtCore import QSemaphore
#from tables import *
import time
# temp
import threading

Base = declarative_base()

class Database:
    def __init__(self, dbfilename):
        
        try:
            self.connect(dbfilename)
            #setup_all()
            #create_all()
        
        except Exception as e:
            print('[-] Could not create database. Please try again.')
            print(e)

    def openDB(self, dbfilename):
        
        try:
            self.connect(dbfilename)
            #setup_all()
        
        except Exception as e:
            print('[-] Could not open database file. Is the file corrupted?')
            print(e)

    def connect(self, dbfilename):
        self.name = dbfilename
        self.dbsemaphore = QSemaphore(1)                            # to control concurrent write access to db
        self.engine = create_engine('sqlite:///'+dbfilename, connect_args={"check_same_thread": False})
        self.session = scoped_session(sessionmaker())
        self.session.configure(bind=self.engine, autoflush=False)
        self.metadata = Base.metadata
        self.metadata.create_all(self.engine)
        self.metadata.echo = True
        self.metadata.bind = self.engine


    # this function commits any modified data to the db, ensuring no concurrent write access to the DB (within the same thread)
    # if you code a thread that writes to the DB, make sure you acquire/release at the beginning/end of the thread (see nmap importer)
    def commit(self):
        self.dbsemaphore.acquire()

        try:
            session = self.session
            session.commit()
        
        except Exception as e:
            print("[-] Could not commit to DB.")
            print(e)

        self.dbsemaphore.release()
