import os

class Manager:
    def __init__(self):
        if not os.path.exists("data"):
            os.mkdir("data")

        if not os.path.isfile("data/config.json"):
            with open("data/config.json", "w") as f:
                f.write("{}")
        
        if not os.path.isfile("data/access.json"):
            with open("data/access.json", "w") as f:
                f.write("{}")