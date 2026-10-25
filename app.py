from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = """
        <!DOCTYPE html>
        <html>
        <head><title>CCA2 Project</title></head>
        <body style="text-align:center; padding-top:50px; font-family:sans-serif;">
            <h1 style="color:#2b5876;">CCA2 CI/CD Deployment</h1>
            <h2>Version: 1.0</h2>
            <p>Automated pipeline running via Jenkins & Minikube.</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 3000), MyHandler)
    print("Server running on port 3000...")
    server.serve_forever()