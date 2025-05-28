# api/main.py
from http.server import BaseHTTPRequestHandler
import json

# Ini adalah fungsi yang akan dipanggil oleh Vercel
# Saat Anda memanggil /api/main.py (atau rute yang mengarah ke sini)
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Hello from Python Serverless Function!"}).encode('utf-8'))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "POST received by Python Function!"}).encode('utf-8'))
