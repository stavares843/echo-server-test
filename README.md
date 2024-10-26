# echo-server-test

[![Unit Tests](https://github.com/stavares843/echo-server-test/actions/workflows/unit-tests.yml/badge.svg?branch=main)](https://github.com/stavares843/echo-server-test/actions/workflows/unit-tests.yml)

This adds a server that listens for incoming requests. Whenever we send it an HTTP request, will respond by sending back everything you sent it — your request path, headers, and so forth.

OS used: Windows 11

# Requirements to run the echo_server.py locally:
- have Python3 installed, cd to this repo and execute `python3 echo_server.py`

# Requirements to run the tests locally:
- have Python3 installed
- have `requests` module - `pip install requests`
- cd to this repo
- execute `python3 -m unittest discover -s . -p "test_server.py"`

# Requirements to compile the binary
- have Python3 installed
- install the `installer` module - `pip install pyinstaller`
- cd to this repo
- execute `pyinstaller --onefile echo_server.py` - this will this will create a `dist` folder where you find the `echo_server.exe`


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


<img width="762" alt="Captura de ecrã 2024-10-26, às 17 31 44" src="https://github.com/user-attachments/assets/2f6e22d2-c3b4-4a9d-add4-dfa56b4dd5fe">

<img width="779" alt="Captura de ecrã 2024-10-26, às 17 32 23" src="https://github.com/user-attachments/assets/b0e2dbed-9662-470c-869d-9e4a59468766">

<img width="867" alt="Captura de ecrã 2024-10-26, às 17 33 25" src="https://github.com/user-attachments/assets/ee701dd4-dd15-435b-b017-fe0805725f7e">
