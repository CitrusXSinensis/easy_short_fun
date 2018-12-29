from PIL import Image

def pixel_char(red, green, blue, alpha = 256):
	# This is the list of chars used to replace pixels in different grey scales
	my_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
	if alpha == 0:
		return ' '

		grey = int((2126 * red + 7152 * green + 722 * blue) / 10000)

		unit = (256 + 1)/ 70

		return my_char[int(grey/unit)]

def char_image(input, width, height):
	im = Image.open(input)
	im = im.resize((width, height), Image.NEAREST)

	txt_image = ""

	for row in range(height):
		for col in range(width):
			txt += pixel_char(*im.getpixel((width, height)))
		txt += '\n'

	print(txt)
