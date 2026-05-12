from http.server import BaseHTTPRequestHandler, HTTPServer
from areacalculator import square
area = square(5)
print("The area of the square is:", area)


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(
            bytes("<h1>area of square: " + str(area) + "</h1>", "utf-8"))


server = HTTPServer(("localhost", 8000), MyServer)

print("Server running at http://localhost:8000")


server.serve_forever()
