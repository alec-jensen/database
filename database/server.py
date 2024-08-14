from webserver import Request, Webserver
import json

from manager import Manager

class Server:
    def __init__(self, manager: Manager): 
        self.server = server = Webserver("0.0.0.0", 8080)
        self.manager = manager

    def start(self):
        self.server.start()
