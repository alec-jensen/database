from webserver import Request, Webserver, Response, ResponseCodes
import json
import hashlib
import hmac

from manager import Manager

class Server:
    def __init__(self, manager: Manager):
        self.server = Webserver("0.0.0.0", 8080)
        self.manager = manager

        @self.server.get("/{collection}/fetch_one")
        async def fetch_one(request: Request, collection: str):
            if not self._authenticate(request):
                return Response("Unauthorized", status=ResponseCodes.UNAUTHORIZED)
            
            try:
                query = json.loads(request.body)
            except json.JSONDecodeError:
                return Response("Invalid JSON", status=ResponseCodes.BAD_REQUEST)
            
            doc = self.manager.fetch_one(collection, query)

            response = Response(json.dumps({
                "status": "success",
                "document": doc
            }), headers={"Content-Type": "application/json"})

            return response
        
        @self.server.post("/{collection}/insert_one")
        async def insert_one(request: Request, collection: str):
            print(request.headers)
            if not self._authenticate(request):
                return Response("Unauthorized", status=ResponseCodes.UNAUTHORIZED)
            
            try:
                document = json.loads(request.body)
            except json.JSONDecodeError:
                return Response("Invalid JSON", status=ResponseCodes.BAD_REQUEST)
            
            self.manager.insert_one(collection, document)

            response = Response(json.dumps({
                "status": "success"
            }), headers={"Content-Type": "application/json"})

            return response

    def start(self):
        self.server.start()

    def _authenticate(self, request: Request):
        if "Authorization" not in request.headers:
            return False
        
        key_id, key = request.headers["Authorization"].split("+")

        with open("data/access.json", "r") as f:
            access = json.load(f)

        for key_item in access["keys"]:
            if key_item["id"] == key_id:
                if hmac.compare_digest(hashlib.sha256(key.encode()).hexdigest(), key_item["hash"]):
                    return True
