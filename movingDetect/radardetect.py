#!/usr/bin/env python2

import sys
import numpy as np
import skimage
from skimage import io
from skimage.viewer import ImageViewer
from colors import colors

def isSameColor( color1 , color2 , color_err):
    if ( abs(color1[0] - color2[0]) <= color_err and
         abs(color1[1] - color2[1]) <= color_err and
         abs(color1[2] - color2[2]) <= color_err ) : 
        return True
    else :
        return False

def diffusion( color , graph , error ):
    color_err = 10

    [row,col,temp] = graph.shape
    canvas   = np.zeros([row,col],dtype='int')

    for i in range(row):
        for j in range(col):
            if ( i < 167 and j < 63 ):
                continue
            if ( i < 324 and j < 50 ):
                continue
            if ( isSameColor( graph[i,j] , color , color_err ) ) :
                lrow = max(  0    , i-error   )
                mrow = min( row-1 , i+error+1 )
                lcol = max(  0    , j-error   )
                mcol = min( col-1 , j+error+1 )
                canvas[ lrow:mrow , lcol:mcol ] = 1
    return canvas

graph_path = [ 'img/2015-08-22_2306.2MOS3NC.jpg' ,
               'img/2015-08-22_2312.2MOS3NC.jpg' 
             ]
graph = [ io.imread(graph_path[0]) , io.imread(graph_path[1])]
canvas  = []
for i in range(len(colors)) :
    canvas1    = diffusion( colors[i]['color'] , graph[0] , colors[i]['error'])
    canvas2    = diffusion( colors[i]['color'] , graph[1] , colors[i]['error'])
    canvast    = canvas2 - canvas1
    canvastF   = canvast < 0
    canvast[canvastF] = 0
    canvast    = canvast | canvas2 
    canvas.append( np.array(canvast,'bool') )

[row,col,temp] = graph[0].shape
result = np.zeros([row,col,3],dtype='int')
for i in range(row):
    for j in range(col) :
        for color in range(len(colors)):
            if ( canvas[color][i,j] == True ):
                result[i,j] = [ 
                    max( result[i,j][0] , colors[color]['intensity']),
                    0,
                    0
                ]


resultFilter = result > 255
result[resultFilter] = 255
io.imsave('result.jpg' , np.array( result , 'uint8' ) )
