# echo-server-test


This adds a server that listens for incoming requests. Whenever we send it an HTTP request, will respond by sending back everything you sent it — your request path, headers, and so forth.

The server is written in Python and listens on port 8080.

Requests:
- GET request, it echoes back the requested path and the headers.
- POST request, it echoes back any data additional to the headers.

How to use:
- clone repo
- go to repo
- go to this branch
- run `python3 echo_server.py`

Once it’s running, you can send requests to it, like typing http://localhost:8080/test in the browser or executing a curl to test it.

Example

<img width="555" alt="Captura de ecrã 2024-10-25, às 13 03 55" src="https://github.com/user-attachments/assets/c16797db-5198-4587-8337-533c9c1dd1fb">

<img width="711" alt="Captura de ecrã 2024-10-25, às 13 04 14" src="https://github.com/user-attachments/assets/5f34c817-6cf6-4689-904e-114b6d3ba593">

<img width="1149" alt="Captura de ecrã 2024-10-25, às 13 11 18" src="https://github.com/user-attachments/assets/c12177e9-9ff8-48d2-a3cf-a82b1e96f12b">

