"""Optional local-only manual trigger, not enabled in Railway production.

Runs inside the SAME container and persistent volume as the cron executor.
A separate Railway service must never use this handler.
"""
import hmac
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from .execute_once import execute

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/internal/manual-scan":
            self.send_error(404)
            return
        secret = os.environ.get("SIMPLE_SCANNER_TRIGGER_TOKEN", "")
        provided = self.headers.get("Authorization", "")
        if not secret or not hmac.compare_digest(provided, "Bearer " + secret):
            self.send_error(401)
            return
        if self.headers.get("Content-Length") not in ("0", None):
            self.send_error(400)
            return
        result = execute("manual")
        status = 202 if result == 0 else 409 if result == 75 else 503
        body = json.dumps({"execution_exit_code": result, "accepted": result == 0}).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

def serve():
    # Loopback only: requires an explicitly authenticated proxy for remote access.
    server = ThreadingHTTPServer(("127.0.0.1", 8765), Handler)
    server.serve_forever()

if __name__ == "__main__":
    serve()
