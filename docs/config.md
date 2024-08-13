# The config file
The config file is a JSON file inside the `data` folder that contains the configuration for the database. The following fields are supported:

```json
{
    "host": "localhost",
    "port": 8080
}
```

## access.json options
This file is managed by the `generate_api_key` utility script. If you want to manually edit it, the following fields are supported: 

```json
{
    "keys": [
        {
            "hash": "some hash",
            "comment": "This is a comment to help you identify the key",
            "permissions": ["read", "write", "delete"],
            "expires": 123456789, // Unix timestamp
            "allowed_ips": ["*"]
        }
    ]
}
```