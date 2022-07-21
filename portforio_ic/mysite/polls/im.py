from PIL import Image
import os


def im_to_monokuro(im):
    savename = 'gray.png'

    imgpath = "."+im
    img = Image.open(imgpath)
    gray_img = img.convert('L')
    dirname = os.path.dirname(imgpath)
    gray_img.save(dirname+"/"+savename)
    return savename