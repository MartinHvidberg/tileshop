from PIL import Image
import ts_base as ts

print ts.version()
print ts.helptext()

im_1 = ts.clip("../data/Steward.jpg",100,100,300,300)
im_2 = ts.clip("../data/Asis.png", 0, 0, 300, 300)
im_mask = ts.clip("../data/hole.png", 0,0,300,300).convert('1')
#print im_mask.getcolors(8)
#ts.mask(im_2, im_mask, im_1).show()

# Tile grabber
x,y,ii,jj = (64,96,8,4)
for i in range(ii):
    for j in range(jj):
        im_milieu = ts.clip("../data/tiles.png",i*x,j*y,x,y)
        im_milieu.save("../data/milieu_{}_{}.png".format(i,j),"PNG")
        if i == 3 and j == 2:
            #im_milieu.show()
            im_milieu_51_cc = ts.clip("../data/milieu_{}_{}.png".format(i,j),16,16,32,32)
            #im_milieu_51_cc.show()
            print im_milieu_51_cc.mode, im_milieu_51_cc.size
            im_plate = ts.make(320,320)
            print im_plate.mode, im_plate.size 
            #im_plate.paste(im_milieu,(100,100))
            for k in range(0,320,32):
                for l in range(0,320,32):
                    im_plate = ts.fill(im_plate, im_milieu_51_cc, k, l)
            im_plate.show()
            
# ---
# Image.point(lut, mode=None)
# Maps this image through a lookup table or function.

