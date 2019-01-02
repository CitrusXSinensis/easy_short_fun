import sys
import os
import time
import threading
import termios
import tty
import cv2
import pyprind

class CharFrame:
	ascii_char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

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
