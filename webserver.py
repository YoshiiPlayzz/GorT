from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from os.path import exists
from pathlib import Path


class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        if exists(f"gui/{self.path}"):
            path = self.path
            if path == "/":
                    path = "/index.html"
            if Path(f"gui{path}").is_file():
                

                self.send_response(200)
        
                self.end_headers()

                with open(f"gui{path}", "rb") as f:
                    if f:
                        while(byte := f.read(1)):
                            self.wfile.write(byte)
            else:
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                with open(f"gui/404.html", "rb") as f:
                    if f:
                        while(byte := f.read(1)):
                            self.wfile.write(byte)
        else: 
          self.send_response(200)
          self.send_header("Content-Type", "text/html")
          self.end_headers()
          with open(f"gui/404.html", "rb") as f:
              if f:
                  while(byte := f.read(1)):
                      self.wfile.write(byte)
     

def runServer(host_name, port):
    webServer = HTTPServer((host_name, port), WebServer)

    try:
        print(f"Started server: http://{host_name}:{port}/")
        webServer.serve_forever()
    
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")