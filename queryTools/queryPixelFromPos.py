#!/usr/bin/env python2

import sys
import skimage
from skimage import io

def projection( O , A , B , Z ):
    x1 = A[0] - O[0]
    y1 = A[1] - O[1]
    x2 = B[0] - O[0]
    y2 = B[1] - O[1]
    x3 = Z[0] - O[0]
    y3 = Z[1] - O[1]

    m  = 1/(x1*y2-x2*y1) *( y2*x3  - x2*y3 )
    n  = 1/(x1*y2-x2*y1) *( -y1*x3 + x1*y3 )
    
    return [m,n]

def getPixel( O , A , B , Op , Ap , Bp , m , n ):

    # OA,OB,O'A',O'B'
    X    = [ A[0]  - O[0]  , A[1]  - O[1]  ]
    Y    = [ B[0]  - O[0]  , B[1]  - O[1]  ]
    Xp   = [ Ap[0] - Op[0] , Ap[1] - Op[1] ]
    Yp   = [ Bp[0] - Op[0] , Bp[1] - Op[1] ]
    # |X| , |Y|
    X_l  = ( X[1]  ** 2 + X[1]  ** 2 ) ** 0.5 
    Y_l  = ( Y[0]  ** 2 + Y[1]  ** 2 ) ** 0.5
    Xp_l = ( Xp[0] ** 2 + Xp[1] ** 2 ) ** 0.5 
    Yp_l = ( Yp[0] ** 2 + Yp[1] ** 2 ) ** 0.5
    # coefficient of alpha = |X| / |X_p|
    # Z = mX+nY = maX' + nbY' = Z'       
    # Pixel Position
    px   = m * Xp[0] + n * Yp[0] + Op[0]
    py   = m * Xp[1] + n * Yp[1] + Op[1]
    
    return [round(px),round(py)]

    
    
# Pixel Position and Lat/Lon Position
# O  / A  / B
# O' / A' / B'
Op = [153,261]
Ap = [317,89 ]
Bp = [462,247]
O  = [24.438733,120.623633]
A  = [25.117488,121.281154] 
B  = [24.484190,121.860073]
Z  = [ float(sys.argv[1]) , float(sys.argv[2]) ]
[m , n] = projection(O,A,B,Z)
[px,py] = getPixel(O,A,B,Op,Ap,Bp,m,n)

# Handle Graph
img_path = 'test.jpg' 
graph  = io.imread(img_path)
print ( [px,py] )
print ( graph[py,px] )
