import sys
import os
import time
import threading
import termios
import tty
import cv2
import pyprind

# CharFrame is used to convert each frame to frame made by chars
class CharFrame:
	ascii_char = "#@$=+-\"'^` "

	# convert a single pixel to char
	def pixelToChar(self, luminance):
		return self.ascii_char[int(luminance*len(self.ascii_char)/256)]

	# convert a frame to ascii frame
	def convertFrame(self, image, upperSize=-1, fill=False, wrap=False):
		# resize image if it is larger than upperSize
		if upperSize != -1 and (image.shape[0] > upperSize[1] or image.shape[1] > upperSize[0]):
			image = cv2.resize(image, upperSize, interpolation=cv2.INTER_AREA)
		ascii_frame = ''
		blank = ''
		if fill: blank += ' '*(upperSize[0] - image.shape[1])
		if wrap: blank += '\n'
		for i in range(image.shape[0]):
			for j in range(image.shape[1]):
				ascii_frame += self.pixelToChar(image[i, j])
			ascii_frame += blank
		return ascii_frame

# ImageToChar is used to convert an image to ascii-art image
class ImageToChar(CharFrame):
	result = None
	def __init__(self, path, upperSize=-1, fill=False, wrap=False):
		self.genCharImage(path, upperSize, fill, wrap)

	def genCharImage(self, path, upperSize=-1, fill=False, wrap=False):
		image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
		if image == None: return
		self.result = self.convert(image, upperSize, fill, wrap)

	def showImage(self, stream = 2):
		if self.result == None: return
		if stream == 1 and os.isatty(sys.stdout.fileno()):
                        self.streamOut = sys.stdout.write
                        self.streamFlush = sys.stdout.flush
		elif stream == 2 and os.isatty(sys.stderr.fileno()):
                        self.streamOut = sys.stderr.write
                        self.streamFlush = sys.stderr.flush
		elif hasattr(stream, 'write'):
                        self.streamOut = stream.write
                        self.streamFlush = stream.flush
		self.streamOut(self.result)
		self.streamFlush()
		self.streamOut('\n')

# VideoToChar is used to convert a video to ascii anime
class VideoToChar(CharFrame):
	charVideo = []
	frameRate = 0.033
	def __init__(self, path):
		if path.endswith('txt'): self.load(path)
		else: self.genCharVideo(path)

	def genCharVideo(self, path):
		self.charVideo = []
		cap = cv2.VideoCapture(path)
		self.frameRate = round(1/cap.get(5), 3)
		frameCount = int(cap.get(7))
		print('Generating assci art...')
		for i in pyprind.prog_bar(range(frameCount)):
			frame = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
			charFrame = self.convertFrame(frame, os.get_terminal_size(), fill=True)
			self.charVideo.append(charFrame)
		cap.release()