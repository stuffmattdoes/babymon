from http import server
from io import BytesIO
import logging
# import numpy as np
import os
# import pyaudio
import picamera
import socketserver
from threading import Condition

# Example from https://picamera.readthedocs.io/en/release-1.13/recipes2.html#web-streaming

# chunk=4096
# RATE=44100

# p = pyaudio.PyAudio()

# # input stream setup
# stream = p.open(format = pyaudio.paInt16, rate = RATE, channels = 1, input_device_index = 2, input = True, frames_per_buffer = chunk)

# # output stream setup
# player = p.open(format = pyaudio.paInt16, rate = RATE, channels = 1, output = True, frames_per_buffer = chunk)

# # Used to continuously stream audio
# while True:
#     data = np.fromstring(stream.read(chunk, exception_on_overflow = False), dtype = np.int16)
#     player.write(data, chunk)
    
# closes streams
# stream.stop_stream()
# stream.close()
# p.terminate

class AudioOutput(object):
    def __init__(self):
        self.buffer = BytesIO()       
        self.condition = Condition()

    def write(self, buf):
        return

class VideoOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = BytesIO()
        self.condition = Condition()
        # print(vars(object))
        
    def write(self, buf):
        # print('write!', buf)        
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content 
            # and notify all clients it's available
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
            # print(os.curdir + os.sep + index)
            f = open(os.curdir + os.sep + index, 'rb')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', os.path.getsize(index))
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        elif self.path == '/audio.wav':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()

        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with videoOut.condition:
                        videoOut.condition.wait()
                        frame = videoOut.frame
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

with picamera.PiCamera(framerate = 24, resolution = '640x480') as camera:
    videoOut = VideoOutput()
    camera.rotation = 90
    camera.start_recording(videoOut, format = 'mjpeg')
    
    try:
        address = ('', 80)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
