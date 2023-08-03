
""" Prepares the image data needed for subcut testing and demonstrating """

import os
from PIL import Image
from PIL import ImageFilter

print(f"Pillow ver.: {Image.__version__}")

ROOT_DATA = r"../data/training"  # The root data dictionary
EXT = "_p.jpg"  # The file extension of the images

def filter1(image):
    out = im.filter(ImageFilter.DETAIL)

def wtf(im):
    """ No Clue ... """
    # split the image into individual bands
    source = im.split()

    R, G, B = 0, 1, 2

    # select regions where red is less than 100
    mask = source[R].point(lambda i: i < 100 and 255)

    # process the green band
    out = source[G].point(lambda i: i * 0.7)

    # paste the processed band back, but only where red was < 100
    source[G].paste(out, None, mask)

    # build a new multiband image
    im = Image.merge(im.mode, source)


    imout = im.point(lambda i: expression and 255)  # Note the syntax used to create the mask:


def prep_main():
    # # directory = os.fsencode(directory_in_str)
    for file in sorted(os.listdir(ROOT_DATA)):
        str_fn = os.fsdecode(file)
        if str_fn.endswith(EXT):
            str_ffn = os.path.join(ROOT_DATA, str_fn)
            im = Image.open(str_ffn)
            print(f"img:{str_ffn}: format:{im.format}, size:{im.size}, mode:{im.mode}")
            if "copen" in str_fn:
                print("Copenhagen")
                im.show()
                imf = wtf(im)
                imf.show()
        else:
            continue


if __name__ == "__main__":
    prep_main()
