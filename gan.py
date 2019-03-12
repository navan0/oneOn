from PIL import Image
epoches = 2


def paste_image(image):
    for i in range(epoches):
        imageM = Image.fromarray(image)  # converting numpy array into PIL
        im2 = Image.open('/home/navaneeth/work/oneon/1.png')
        imageM.paste(im2, box=None)
        imageM.save("./detected/gan_"+str(i)+".png", "PNG")
    return 0
