from maxFilledRect import maximalFilledRectangle
from generateTestRect import generate
import numpy
import cv2

pilImage = generate((256,256))
im = numpy.asarray(pilImage)
orig = im.copy()
im2 = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

ret,im2 = cv2.threshold(im2,127,255,cv2.THRESH_BINARY)

(x,y),(w,h) = maximalFilledRectangle(im2, 255)
print (x,y),(w,h)
cv2.rectangle(orig, (x,y), (x-w,y-h), (255,0,0), 5) 
cv2.imwrite("out.png", orig)



