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

def diffusion( color , graph ):
    error     = 10
    color_err = 10

    [row,col,temp] = graph.shape
    canvas   = np.zeros([row,col,3],dtype='int')

    for i in range(row):
        for j in range(col):
            if ( isSameColor( graph[i,j] , color , color_err ) ) :
                lrow = max(  0  , i-error   )
                mrow = min( row , i+error+1 )
                lcol = max(  0  , j-error   )
                mcol = min( col , j+error+1 )
                canvas[ lrow:mrow , lcol:mcol ] = color
    return canvas

colors  = [ 
              { "color" : [254, 0 , 0 ] , "value" : 40 }, 
              { "color" : [199, 0 , 0 ] , "value" : 45 }, 
              { "color" : [149, 1 , 0 ] , "value" : 50 }, 
              { "color" : [253, 0 ,249] , "value" : 55 }, 
              { "color" : [153, 0 ,255] , "value" : 60 }, 
              { "color" : [255,255,255] , "value" : 65 }, 
          ]

graph_path = [ 'a.jpg' , 'b.jpg' ]
graph = [ io.imread(graph_path[0]) , io.imread(graph_path[1])]
canvas  = []
for i in range(len(colors)) :
    canvas1    = diffusion( colors[i]['color'] , graph[0] )
    canvas2    = diffusion( colors[i]['color'] , graph[1] )
    canvast    = canvas2 - canvas1
    canvastF   = canvast < 0 
    canvast[canvastF] = 0
    canvas.append( canvast )
    viewer     = ImageViewer(canvas[i])
    viewer.show()

