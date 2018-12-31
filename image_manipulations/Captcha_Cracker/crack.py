from PIL import Image
import vector_compare
import os

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

def vector_crack(image,colour1,colour2=256):
    v = VectorCompare()
    iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    imageset = []

    # create imageset by using vector_compare module used to compare with elements in captcha
    for letter in iconset:
        for img in os.listdir('./iconset/%s/'%(letter)):
            temp = []
            if img != "Thumbs.db" and img != ".DS_Store":
                temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
            imageset.append({letter:temp})

    im = Image.open("captcha.gif")

    # create a new white image with the same size of captcha
    im2 = Image.new("P",im.size,255)

    im.convert("P")
    temp = {}

    # make im2 to be balck-white image with only wanted element on it
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y,x))
            temp[pix] = pix
            if pix == colour1 or pix == colour2:
                im2.putpixel((y,x),0)

    inletter = False
    foundletter=False
    start = 0
    end = 0

    letters = []

    # get the location of each elements in captcha
    for y in range(im2.size[0]): # slice across
        for x in range(im2.size[1]): # slice down
            pix = im2.getpixel((y,x))
            if pix != 255:
                inletter = True

    if foundletter == False and inletter == True:
        foundletter = True
        start = y

    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start,end))


    inletter=False

    # compare each cropped element with training data we have and prints out the best guess
    for letter in letters:
        im3 = im2.crop((letter[0],0,letter[1],im2.size[1]))

        guess = []

        for image in imageset:
            for x,y in image.iteritems():
                if len(y) != 0:
                    guess.append((v.relation(y[0],buildvector(im3)),x))
        guess.sort(reverse=True)
        print "",guess[0]
            
