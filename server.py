"""Simple static web server built on Python's standard library.

Serves files from the ``public`` directory using ``http.server`` only
(no external web framework). Run with ``python server.py``.
"""

import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlsplit

HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "8000"))
MESSAGE = os.environ.get("MESSAGE", "เว็บเริ่มทำงานแล้ว")
PUBLIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PUBLIC_DIR, **kwargs)

    def do_GET(self):
        if urlsplit(self.path).path == "/message":
            message = MESSAGE.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(message)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(message)
            return
        super().do_GET()


def main():
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Serving '{PUBLIC_DIR}' on http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    main()
