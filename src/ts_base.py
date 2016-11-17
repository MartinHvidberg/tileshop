
str_version = "0.0.2 (Steward)"
str_build   = "2016-11-17 20:00"

str_help = """*** Tile Shop ***
    A simple - yet cool - way to build some tiles for cover your 2D game board...
    For more information. Visit https://bitbucket.org/MartinHvidberg/tileshop
    /Martin
"""

def version():
    return "Version: "+str_version+" Build: "+ str_build

def helptext():
    return str_help

def clip(pic, ofsx, ofsz, margx, margy):
    """ Clip a rectangel out of a picture, and save it to a new file.
    pic = input picture
    --offsetx, --offsety = coordinate shift, in pixels (negative values shift left, down)
    --marginx, --marginy = margins around (left and buttom) each clip-line.
    """
    return

def mask(pic, mask, fill, ofsx, ofsy):
    """    pic = input picture
    mask = mask. Can be picture, can be?
           mask value is black (hex:FFFFFF)
    fill = fill. Can be picture, can be colour value, can be?
    --offsetmx, --offsetmy = mask coordinate shift, in pixels (negative values shift left, down)
    --offsetfx, --offsetfy = fill coordinate shift, in pixels (negative values shift left, down)
    outputs a picture witch is identical to pic, but have all pixels in mask replaced with fill """
    return

def jointiles(i,j,k):
    """Join multible pictures into one picture"""
    return

def batchfile(batch_file):
    """Reads the text file batch-file, and execute it, line by line."""
    return

def maskgenerator(l,m,n):
    """Generates mask files, eg. with random patterns for smooth transects."""
    return
