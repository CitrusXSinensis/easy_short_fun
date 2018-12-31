from PIL import Image

# verify_colour(image) consumes the image of captcha, then prints out the
#   the possible colours we want from the captcha
def verify_colour(image):
    im = Image.open(image)
    im.convert("P")
    histo = im.histogram()
    value = {}
    for i in range(256):
        values[i] = histo[i]

    for j,k in sorted(values.items(),key=lambda x:x[1],reverse = True)[:10]:
        print j,k


