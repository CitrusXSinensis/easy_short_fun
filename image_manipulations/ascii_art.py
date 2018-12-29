from PIL import Image

# pixel_char consumes the RGB scales of a pixel, converts it into grey scale, then returns the char
#   corresponding to the grey scale from my_char list
def pixel_char(red, green, blue, alpha = 256):
	# This is the list of chars used to replace pixels in different grey scales
	my_char = list("#=~-.")
	if alpha == 0:
		return ' '
		# determine the grey scale for the pixel
		grey = int((2126 * red + 7152 * green + 722 * blue) / 10000)
		# as we have 6 different chars
		unit = (256 + 1)/ 5

		return my_char[int(grey/unit)]

	
# char_image consumes the name of image, the width and height of ascii art, then 
#   returns the ascii art with given width and height
def char_image(input, width, height):
	im = Image.open(input)
	# resize the image to size we want for the ascii art
	im = im.resize((width, height), Image.NEAREST)

	txt_image = ""

	for row in range(height):
		for col in range(width):
			txt_image += pixel_char(*im.getpixel((width, height)))
		txt_image += '\n'

	print(txt_image)
