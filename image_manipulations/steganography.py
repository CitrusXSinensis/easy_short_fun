from PIL import Image

def transferToEven(image):
    pixels = list(image.getdata())  # get a list in the format [(r,g,b,t),(r,g,b,t)...]
    evenPixels = [(r>>1<<1,g>>1<<1,b>>1<<1,t>>1<<1) for [r,g,b,t] in pixels]  # change all the lsb to 0
    evenImage = Image.new(image.mode, image.size)  # create a new image with the same size
    evenImage.putdata(evenPixels)
    return evenImage

def convertToBin(myInt):
    #remove '0b' in the return value of bin()，and add '0' in the beginning of the string until it has length=8
    myBin = "0"*(8-(len(bin(myInt))-2))+bin(myInt).replace('0b','')
    return myBin


