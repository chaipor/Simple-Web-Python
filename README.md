# Simple-Web-Python

A minimal static web project served by Python's standard library
`http.server` module — no external web framework required.

## Project structure

```text
Simple-Web-Python/
├── public/
│   └── index.html   # Static page served by the server
├── server.py         # Entry point (python server.py)
├── Dockerfile
└── README.md
```

## Run locally

Requires Python 3.9+ (uses only the standard library, no `requirements.txt`
needed).

```powershell
python server.py
```

Then open http://localhost:8000 in your browser.

Optional environment variables:

- `HOST` (default `0.0.0.0`)
- `PORT` (default `8000`)
- `MESSAGE` (default `เว็บเริ่มทำงานแล้ว`): initial message displayed on the page

## Run with Docker

```powershell
docker build -t simple-web-python .
docker run -p 8000:8000 simple-web-python
```

Then open http://localhost:8000.

To set the initial message when starting the container:

```powershell
docker run -p 8000:8000 -e "MESSAGE=สวัสดีจาก Docker" simple-web-python
```

The `message` URL parameter overrides the initial message, for example
http://localhost:8000/?message=Hello. Change the environment variable and
recreate the container to change the initial message.
