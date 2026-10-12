"""Read-only status endpoint plus bounded periodic repair worker."""
import json
import os
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from repair import run_once

REQUIRED = ("AGENT_MODEL_URL", "AGENT_MODEL_TOKEN", "AGENT_MODEL_NAME", "AGENT_GITHUB_TOKEN")
STATE = {"service": "kraken-engineering-agent", "mode": "readiness_only",
         "last_run": None, "last_result": None, "autonomous_repair_enabled": False}
LOCK = threading.Lock()

def configured():
    return all(os.getenv(key) for key in REQUIRED)

def worker():
    while True:
        enabled = os.getenv("AGENT_ENABLED") == "true" and configured()
        with LOCK:
            STATE["autonomous_repair_enabled"] = enabled
            STATE["mode"] = "review_pr_only" if enabled else "readiness_only"
        if enabled:
            try:
                result = run_once()
            except Exception as exc:
                result = {"status": "error", "type": type(exc).__name__, "details": str(exc)[:300]}
            with LOCK:
                STATE["last_run"] = int(time.time())
                STATE["last_result"] = result
        time.sleep(max(900, int(os.getenv("AGENT_INTERVAL_SECONDS", "3600"))))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/health", "/status"):
            self.send_error(404)
            return
        with LOCK:
            payload = dict(STATE)
        payload["configured"] = configured()
        payload["missing_configuration"] = [key for key in REQUIRED if not os.getenv(key)]
        if self.path == "/health":
            payload = {"ok": True, "mode": payload["mode"]}
        data = json.dumps(payload).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

if __name__ == "__main__":
    threading.Thread(target=worker, daemon=True).start()
    HTTPServer(("0.0.0.0", int(os.getenv("PORT", "8080"))), Handler).serve_forever()
