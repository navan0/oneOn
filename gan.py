from PIL import Image
epoches = 2


def paste_image(image):
    for i in range(epoches):
        imageM = Image.fromarray(image)  # converting numpy array into PIL image
        im2 = Image.open('./1.png')
        x, y = im2.size
        imageM.paste(im2, box=None)
        imageM.save("./detected/test_"+str(i)+".png", "PNG")
    return 0
