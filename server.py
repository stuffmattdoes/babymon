import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server
from os import curdir, sep

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            index = 'index.html'
            f = open(curdir + sep + index)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            # self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()

        # try:
		# 	#Check the file extension required and
		# 	#set the right mime type

		# 	sendReply = False
		# 	if self.path.endswith('.html'):
		# 		mimetype='text/html'
		# 		sendReply = True
		# 	if self.path.endswith('.jpg'):
		# 		mimetype='image/jpg'
		# 		sendReply = True
		# 	if self.path.endswith('.gif'):
		# 		mimetype='image/gif'
		# 		sendReply = True
		# 	if self.path.endswith('.js'):
		# 		mimetype='application/javascript'
		# 		sendReply = True
		# 	if self.path.endswith('.css'):
		# 		mimetype='text/css'
		# 		sendReply = True

		# 	if sendReply == True:
		# 		#Open the static file requested and send it
		# 		f = open(curdir + sep + self.path) 
		# 		self.send_response(200)
		# 		self.send_header('Content-type',mimetype)
		# 		self.end_headers()
		# 		self.wfile.write(f.read())
		# 		f.close()
		# 	return

		# except IOError:
		# 	self.send_error(404,'File Not Found: %s' % self.path)

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    output = StreamingOutput()
    camera.rotation = -90
    camera.start_recording(output, format='mjpeg')
    
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
