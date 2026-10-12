import json, os, time, urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

MODEL_URL=os.getenv("AGENT_MODEL_URL","")
MODEL_TOKEN=os.getenv("AGENT_MODEL_TOKEN","")
REPO=os.getenv("AGENT_REPO","michaelrobinsonproduct-del/Cryptoscanner")
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/health","/status"):
            self.send_error(404);return
        status={"service":"kraken-engineering-agent","mode":"readiness_only","repository":REPO,"model_configured":bool(MODEL_URL and MODEL_TOKEN),"autonomous_repair_enabled":False,"reason":"Model credentials and isolated repair executor must pass acceptance before activation"}
        data=json.dumps(status).encode()
        self.send_response(200);self.send_header("Content-Type","application/json");self.send_header("Content-Length",str(len(data)));self.end_headers();self.wfile.write(data)
if __name__=="__main__":
    HTTPServer(("0.0.0.0",int(os.getenv("PORT","8080"))),Handler).serve_forever()
