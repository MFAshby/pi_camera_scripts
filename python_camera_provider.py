import picamera
import socketserver
import io

HOST = "localhost"
PORT = 8005
FORMAT = 'jpeg'


class CameraServer(socketserver.TCPServer):
    allow_reuse_address = True

    def server_activate(self):
        self.camera_init()
        socketserver.TCPServer.server_activate(self)

    def server_close(self):
        self.camera_close()
        socketserver.TCPServer.server_close(self)

    def camera_init(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (800, 600)
        self.imagebuffer = io.BytesIO()
        self.camera_iterator = self.camera.capture_continuous(self.imagebuffer, format=FORMAT)

    def camera_close(self):
        self.camera.close()

    def next_image(self):
        self.imagebuffer.seek(0)
        self.imagebuffer.truncate()
        next(self.camera_iterator)
        return self.imagebuffer.getbuffer()


class CameraRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        image_data = self.server.next_image()
        self.wfile.write(image_data)


def run_camera_server():
    server = CameraServer((HOST, PORT), CameraRequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
    

if __name__=="__main__":
    run_camera_server()
