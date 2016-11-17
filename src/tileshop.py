
from PIL import Image
import ts_base as ts

print ts.version()
print ts.helptext()

im = Image.open("../data/Steward.jpg")
print im.format, im.size, im.mode
im.show()
