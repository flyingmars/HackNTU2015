#!/usr/bin/env python2

import sys
import numpy as np
import skimage
from skimage import io
from skimage.viewer import ImageViewer

def isSameColor( color1 , color2 , color_err):
    if ( abs(color1[0] - color2[0]) <= color_err and
         abs(color1[1] - color2[1]) <= color_err and
         abs(color1[2] - color2[2]) <= color_err ) : 
        return True
    else :
        return False

def diffusion( color , graphpath ):
    error     = 10
    color_err = 10

    img_path  = graphpath
    graph     = io.imread(img_path)
    [row,col,temp] = graph.shape
    canvas   = np.zeros([row,col,3],dtype='uint8')

    for i in range(row):
        for j in range(col):
            if ( isSameColor( graph[i,j] , color , color_err ) ) :
                lrow = max(  0  , i-error   )
                mrow = min( row , i+error+1 )
                lcol = max(  0  , j-error   )
                mcol = min( col , j+error+1 )
                canvas[ lrow:mrow , lcol:mcol ] = [255,0,0]
    return canvas

red     = [254,0,0]
canvas1 = diffusion( red , 'a.jpg' )
canvas2 = diffusion( red , 'b.jpg' )
canvas3 = canvas2 - canvas1
viewer  = ImageViewer(canvas3)
viewer.show()

