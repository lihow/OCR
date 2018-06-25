#coding:utf-8
#coding:utf-8
import model
from glob import glob
import numpy as np
from PIL import Image
import time
paths = glob('./test/*.*')

def dect(img):
    img = np.array(img.convert('RGB'))
    t = time.time()
    result,img,angle = model.model(img,model='pytorch')
    cost_t = time.time()-t
    return (cost_t, result)

if __name__=='__main__':
    img = Image.open(paths[0])
    cost_t, result = dect(img)
    print "It takes time:{}s".format(cost_t)
    print "---------------------------------------"
    for key in result:
        print result[key][1]
