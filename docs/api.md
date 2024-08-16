# The API
## Authenticating with the API
To authenticate with the API, you need to provide a valid API key in the `Authorization` header of your request. You can generate an API key by running the `generate_api_key` utility script.

## Routes
- GET /{collection}/fetch_one - Fetch the first document from the database, using a JSON query provided in the request body.
- GET /{collection}/fetch_many?count=X - Fetch the first X documents from the database, using a JSON query provided in the request body.
- POST /{collection}/insert_one - Insert a document into the database, using a JSON document provided in the request body.
- POST /{collection}/insert_many - Insert multiple documents into the database, using a JSON array of documents provided in the request body.
- PUT /{collection}/update_one - Update a document in the database, using a JSON query and a JSON update document provided in the request body.
- DELETE /{collection}/delete_one - Delete a document from the database, using a JSON query provided in the request body.
- DELETE /{collection}/delete_many - Delete multiple documents from the database, using a JSON query provided in the request body.