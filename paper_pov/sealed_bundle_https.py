"""Read-only TLS delivery of the latest verified GitHub paper scan artifact.

Requires PAPER_BUNDLE_TOKEN, TLS certificate/key and authenticated gh CLI.
No scan, ledger writer, or deployment is started by importing this module.
"""
import argparse
import datetime as dt
import hmac
import json
import os
import ssl
import subprocess
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from paper_pov.github_sealed_bundle_readback import read_run


def latest_run(repo, runner=subprocess.check_output):
    raw = runner(["gh", "run", "list", "-R", repo, "-w", "paper-pipeline.yml",
                  "--limit", "10", "--json",
                  "databaseId,status,conclusion,headBranch,event"])
    runs = json.loads(raw)
    eligible = [x for x in runs if x.get("status") == "completed"
                and x.get("conclusion") == "success"
                and x.get("headBranch") == "main"
                and x.get("event") in ("schedule", "workflow_dispatch")]
    if not eligible:
        raise ValueError("no successful authoritative paper scan")
    return str(max(int(x["databaseId"]) for x in eligible))


def make_handler(repo, token, *, resolver=latest_run, reader=read_run):
    if not token or len(token) < 32:
        raise ValueError("PAPER_BUNDLE_TOKEN must be at least 32 characters")
    gate = threading.Lock()
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path != "/sealed-paper":
                self.send_error(404)
                return
            auth = self.headers.get("Authorization", "")
            if not hmac.compare_digest(auth, "Bearer " + token):
                self.send_response(401)
                self.send_header("Cache-Control", "no-store")
                self.send_header("WWW-Authenticate", "Bearer")
                self.end_headers()
                return
            try:
                with gate:
                    record = reader(repo, resolver(repo))
                bundle = record["bundle"]
                report = json.loads(bundle["receipt_json"])
                stamp = dt.datetime.fromisoformat(report["as_of"].replace("Z", "+00:00"))
                age = (dt.datetime.now(dt.timezone.utc) - stamp).total_seconds()
                if stamp.tzinfo is None or not 0 <= age <= 600:
                    raise ValueError("stale paper receipt")
                data = json.dumps(bundle, separators=(",", ":"), allow_nan=False).encode()
                if len(data) > 1_000_000:
                    raise ValueError("sealed bundle exceeds HTTP reader limit")
            except (ValueError, OSError, subprocess.CalledProcessError, json.JSONDecodeError):
                self.send_response(503)
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                return
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        def log_message(self, fmt, *args):
            pass  # Never log bearer credentials or query strings.
    return Handler


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8443)
    parser.add_argument("--cert", required=True)
    parser.add_argument("--key", required=True)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port),
                                 make_handler(args.repo, os.environ.get("PAPER_BUNDLE_TOKEN", "")))
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(args.cert, args.key)
    server.socket = context.wrap_socket(server.socket, server_side=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
