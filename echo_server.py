import http.server
import socketserver

# Define the request handler class
class EchoHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Echo the request path
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # Write the echo message to the response body
        response = f"Received GET request:\nPath: {self.path}\n\nHeaders:\n{self.headers}"
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        # Read the request body data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Echo the request path, headers, and body
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        response = (
            f"Received POST request:\nPath: {self.path}\n\n"
            f"Headers:\n{self.headers}\n\n"
            f"Body:\n{post_data.decode('utf-8')}"
        )
        self.wfile.write(response.encode('utf-8'))

# Set up the server
PORT = 8080
Handler = EchoHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()

