from http.server import BaseHTTPRequestHandler, HTTPServer
import python_camera_client

PORT_NUMBER = 8000

class WebCamHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'image/jpg')
        self.end_headers()
        image_data = python_camera_client.capture_image()
        self.wfile.write(image_data)


def run_server():
    try:
        server = HTTPServer(('', PORT_NUMBER), WebCamHandler)
        print('Started HTTP server on port ', PORT_NUMBER)
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

if __name__=="__main__":
    run_server()
