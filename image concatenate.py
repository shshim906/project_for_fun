# This code snippet provides functions that concatenate images

from PIL import Image

# get_concat_h will concatenate image horizontally
# im2 will be placed on the right side of im1
def get_concat_h(im1, im2):
    # dst: empty image to paste the images onto
    dst = Image.new('RGBA', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

# get_concat_h will concatenate image vertically
# im2 will be placed on the bottom of im1
def get_concat_v(im1, im2):
    # dst: empty image to paste the images onto
    dst = Image.new('RGBA', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

# TEST
# im1= Image.open('aero.png')
# im2=Image.open('asylum.png')
# ph=Image.open('placeholder.png')


# result=get_concat_h(ph,im1)
# result2=get_concat_v(result,im1)
# result2.show()