from PIL import Image
i=1
TARGER_DIR = '/home/navaneeth/work/oneon/detected'
im1 = Image.open('/home/navaneeth/work/oneon/test.jpg')
im2 = Image.open('/home/navaneeth/work/oneon/1.png')
x, y = im2.size
im1.paste(im2, (0, 0, x, y))
im1.save("/home/navaneeth/work/oneon/detected/test_"+str(i)+".jpg", "JPEG")
