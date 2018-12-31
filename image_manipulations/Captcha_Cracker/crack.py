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

    for letter in iconset:
        for img in os.listdir('./iconset/%s/'%(letter)):
            temp = []
            if img != "Thumbs.db" and img != ".DS_Store":
                temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
            imageset.append({letter:temp})

            
