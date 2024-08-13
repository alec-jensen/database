from webserver import Request, Webserver
import json

class Server:
    server = Webserver("0.0.0.0", 8080)

    def __init__(self) -> None:    
        pass

    def start(self):
        self.server.start()

    @server.get("/fetch_one")
    async def fetch_one(self, request: Request):
        return "fetch_one" + request.body
    
    @server.get("/fetch_many")
    async def fetch_many(self, request: Request, count: int):
        return "fetch_many" + str(count) + request.body
    
    @server.post("/insert_one")
    async def insert_one(self, request: Request):
        return "insert_one" + request.body
    
    @server.post("/insert_many")
    async def insert_many(self, request: Request):
        return "insert_many" + request.body
    
    @server.put("/update_one")
    async def update_one(self, request: Request):
        return "update_one" + request.body
    
    @server.delete("/delete_one")
    async def delete_one(self, request: Request):
        return "delete_one" + request.body
    
    @server.delete("/delete_many")
    async def delete_many(self, request: Request, count: int):
        return "delete_many" + str(count) + request.body