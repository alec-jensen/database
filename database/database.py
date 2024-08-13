from server import Server

class Database:
    def __init__(self) -> None:
        self.server = Server()
        self.server.start()