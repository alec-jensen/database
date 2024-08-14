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

while True:
    allowed_ips = input("Enter a comma-separated list of allowed IP addresses (leave blank for all IPs): ")

    if allowed_ips == "":
        allowed_ips = ["*"]
        break

    allowed_ips = allowed_ips.split(",")

    for ip in allowed_ips:
        for part in ip.split("."):
            if not part.isdigit() or int(part) < 0 or int(part) > 255:
                print("Invalid IP address. Please try again.")
    else:
        break

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
    "allowed_ips": allowed_ips
}

access["keys"].append(key_item)

with open("data/access.json", "w") as f:
    json.dump(access, f, indent=4)

print(f"Secret: {api_key}")
print("API key generated successfully.")
