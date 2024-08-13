import uuid
import hashlib
import json
import os

comment = input("Enter a comment to describe the API key: ")

while True:
    expiry = input("Enter an expiry date for the API key in the UNIX timestamp format (leave blank for no expiry): ")

    if expiry == "":
        expiry = None
        break

    try:
        expiry = int(expiry)
        break
    except ValueError:
        print("Invalid expiry date. Please try again.")

if not os.path.exists("data"):
    os.mkdir("data")

if not os.path.isfile("data/access.json"):
    with open("data/access.json", "w") as f:
        f.write("{}")

with open("data/access.json", "r") as f:
    access = json.load(f)

if access.get("keys") is None:
    access["keys"] = []

api_key = str(uuid.uuid4())
key_hash = hashlib.sha256(api_key.encode()).hexdigest()

key_item = {
    "key": key_hash,
    "comment": comment,
    "permissions": ["read", "write", "delete"],
    "expires": expiry,
    "allowed_ips": ["*"]
}