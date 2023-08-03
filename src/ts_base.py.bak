
from PIL import Image

# http://pillow.readthedocs.io/en/3.1.x/reference/Image.html

str_version = "0.0.3 (Steward)"
str_build   = "2016-11-17 22:00"

str_help = """*** Tile Shop ***
    A simple - yet cool - way to build some tiles for cover your 2D game board...
    For more information. Visit https://bitbucket.org/MartinHvidberg/tileshop
    /Martin
"""

def version():
    return "Version: "+str_version+" Build: "+ str_build

def helptext():
    return str_help

def ooss2lurl(tup_ooss, tup_imsize):
    """offset,offset,size,size 2 left,upper,right,lower"""
    ox, oy, sx, sy = tup_ooss
    imx, imy = tup_imsize
    left = ox
    right = ox + sx
    upper = imy-(oy+sy)
    lower = imy-oy
    return((left,upper,right,lower))
    
def lurl2ooss(tup_lurl, tup_imsize):
    """offset,offset,size,size 2 left,upper,right,lower"""
    left, upper, right, lower = tup_lurl
    imx, imy = tup_imsize
    ox = left
    oy = imy-lower
    sx = right-left
    sy = lower-upper
    return((ox,oy,sx,sy))

def make(sizex=1, sizey=1, mode='RGBA'):
    """ Make new empty picture """
    # Image.new(mode, (sizex,sizey), color) # XXX let make() accept deafult init colour
    return Image.new(mode, (sizex,sizey))
    
def clip(str_pic_file_name, ofsx=0, ofsy=0, sizex=1, sizey=1, margx=0, margy=0, repeat=False):
    """ Clip a rectangel out of a picture, and save it to a new file.
    pic = input picture
    --offsetx, --offsety = coordinate shift, in pixels (negative values shift left, down)
    --marginx, --marginy = margins around (left and buttom) each clip-line.
    """
    """The im.crop() region is defined by a 4-tuple, where coordinates are (left, upper, right, lower). 
    The Python Imaging Library uses a coordinate system with (0, 0) in the upper left corner. 
    Also note that coordinates refer to positions between the pixels, so the region in the 
    (100, 100, 400, 400) is exactly 300x300 pixels."""
    if repeat:
        print "'--repeat' Not implemented  yet..."
        return
    else:
        im = Image.open(str_pic_file_name, 'r')
        #print "im", (im.format, im.size, im.mode)
        lurl = ooss2lurl((ofsx,ofsy, sizex, sizey), im.size)
        #print "lurl:", lurl
    return im.crop(lurl)

def mask(pic, mask, fill):
    """    pic = input picture
    mask = mask. Can be picture, can be?
           mask value is black (hex:FFFFFF)
    fill = fill. Can be picture, can be colour value, can be?
    --offsetmx, --offsetmy = mask coordinate shift, in pixels (negative values shift left, down)
    --offsetfx, --offsetfy = fill coordinate shift, in pixels (negative values shift left, down)
    outputs a picture witch is identical to pic, but have all pixels in mask replaced with fill """
    return Image.composite(pic, fill, mask.convert('1'))

def fill(pic1,pic2,ofsx=0,ofsy=0):
    """Fill (add, stamp) pic2 into pic1. lower-left pixel of pic2 will replace (x,y) pixel in pic1"""
    #return pic1.paste(pic2,ooss2lurl((ofsx,ofsy,pic1.size[0],pic1.size[1]),pic1.size),None)
    print "  pic1:", pic1
    print "  pic2:", pic2
    print "  ofsx:", str(type(ofsy)),ofsy
    print "  ofsy:", str(type(ofsy)),ofsy
    #im_plate.paste(im_milieu,(100,100))
    pic1.paste(pic2,(ofsx,ofsy))
    print pic1 
    return pic1
    #return pic1.paste(pic2)

def tint(pic, oldcolour, newcolour):
    return

def batchfile(batch_file):
    """Reads the text file batch-file, and execute it, line by line."""
    return

def maskgenerator(l,m,n):
    """Generates mask files, eg. with random patterns for smooth transects."""
    # Image.putpixel(xy, value) ?
    # Image.save(fp, format=None, **params)
    return

# Image.rotate(angle, resample=0, expand=0)