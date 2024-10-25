import http.server
import socketserver

# define the request handler class
class EchoHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # echo the request path
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # add echo message to the response body
        response = f"Received GET request:\nPath: {self.path}\n\nHeaders:\n{self.headers}"
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        # read request body data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # echo request path, headers, and body
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        response = (
            f"Received POST request:\nPath: {self.path}\n\n"
            f"Headers:\n{self.headers}\n\n"
            f"Body:\n{post_data.decode('utf-8')}"
        )
        self.wfile.write(response.encode('utf-8'))

def run(server_class=http.server.HTTPServer, handler_class=EchoHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
