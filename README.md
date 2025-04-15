# Python JSON Document Database

A simple document database written from scratch in Python. It stores data as JSON documents and provides a basic HTTP API for interaction. This project utilizes the [webserver](https://github.com/alec-jensen/webserver) library, also written from scratch.

## Features

- [x] JSON document storage.
- [x] HTTP API for CRUD operations.
- [x] Basic API key authentication.
- [x] Simple query mechanism (currently supports exact match).

## Installation

1. **Install uv:**

    [uv installation](https://docs.astral.sh/uv/getting-started/installation/)

2. **Install dependencies:**

    ```bash
    uv venv && uv sync
    ```

## Usage

1. **Generate an API Key:**
    Run the utility script to create an API key for accessing the database. You'll be prompted for details like allowed IPs and expiry.

    ```bash
    uv run utils/generate_api_key.py
    ```

    Keep the generated `Secret` safe, as it's needed for API requests. The key details are stored in `data/access.json`.

2. **Start the Database Server:**

    ```bash
    uv run database/database.py
    ```

    Or use the VS Code debugger configuration provided in `.vscode/launch.json`.

3. **Interact with the API:**
    Use an HTTP client (like `curl`, Postman, or Python's `requests` library) to send requests to the server (default: `http://localhost:8080`). Remember to include the `Authorization` header with your generated key (`KeyID+Secret`).

    Example using `curl` to insert a document:

    ```bash
    curl -X POST http://localhost:8080/my_collection/insert_one \
         -H "Authorization: <Your_KeyID>+<Your_Secret>" \
         -H "Content-Type: application/json" \
         -d '{"name": "Alice", "age": 30}'
    ```

## Documentation

- **[API Endpoints](./docs/api.md):** Details on available HTTP routes.
- **[Configuration](./docs/config.md):** Information about the `config.json` and `access.json` files.
- **[Query Syntax](./docs/queries.md):** Explanation of how to structure queries (currently basic).

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

(Consider adding a license file and specifying it here, e.g., MIT License)