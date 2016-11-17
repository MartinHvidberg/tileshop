#from PIL import Image
import ts_base as ts

print ts.version()
print ts.helptext()

im_clp = ts.clip("../data/Steward.jpg",100,100,200,200)
im_clp.show()
