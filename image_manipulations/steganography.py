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

def decodeBinToStr(myBin):
    string = [chr(int(aBin,2)) for aBin in [myBin[i:i+8] for i in range(0, len(myBin), 8)]]
    return ''.join(string)

def encodeImage(image,data):
    evenImage = transferToEven(image) # get copy of image with lsb changed to 0
    binData = ''.join(map(convertToBin,bytearry(data,'utf-8')))
    if len(binData) > 4 * len(image.getdata()):
        raise Exception("Error: Given " + len(binData) + " bits, but image can only encode " + 4 * len(image.getdata()) + " bits")
    encodedPixels = [(r+int(binData[index*4+0]),g+int(binData[index*4+1]),b+int(binData[index*4+2]),t+int(binData[index*4+3])) if index*4 < len(binary) else (r,g,b,t) for index,(r,g,b,t) in enumerate(list(evenImage.getdata()))] # 将 binary 中的二进制字符串信息编码进像素里
    encodedImage = Image.new(evenImage.mode, evenImage.size)  # create image to store encoded pixels
    encodedImage.putdata(encodedPixels)
    return encodedImage

def decodeImage(image):
    pixels = list(image.getdata())
    binData = ''.join([str(int(r>>1<<1!=r))+str(int(g>>1<<1!=g))+str(int(b>>1<<1!=b))+str(int(t>>1<<1!=t)) for (r,g,b,t) in pixels])
    # find the end of encoded pixels
    doubleNull = binData.find('0' * 16)
    endIndex = doubleNull+(8-(locationDoubleNull % 8)) if doubleNull%8 != 0 else doubleNull
    data = decodeBinToStr(binData[0:endIndex])
    return data
