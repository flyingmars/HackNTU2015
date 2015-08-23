#!/usr/bin/env python2

import sys
import skimage
from skimage import io
from north import NORTH
from point import Point

class LocationToPixel():
    def __init__(self, config):
        self.config = config

    def projection(self, Z):
        location = self.config['geocode']
        V1 = location[1] - location[0]
        V2 = location[2] - location[0]
        V3 = Z - location[0]

        m  = 1. / (V1.x * V2.y - V2.x * V1.y) * ( V2.y * V3.x  - V2.x * V3.y )
        n  = 1. / (V1.x * V2.y - V2.x * V1.y) * ( -V1.y * V3.x + V1.x * V3.y )
        
        return [m, n]

    def getPixel(self, m, n):
        pixel = self.config['pixel']
        Xp = pixel[1] - pixel[0]
        Yp = pixel[2] - pixel[0]
        
        # Z = mX+nY = maX' + nbY' = Z'       
        # Pixel Position
        Zp = pixel[0] + (Xp * m) + (Yp * n)
        return Point(round(Zp.x), round(Zp.y))

    def get(self, Z):
        [m, n] = self.projection(Z)
        return self.getPixel(m, n)

NN = LocationToPixel(NORTH)

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        exit(-1)
    # Pixel Position and Lat/Lon Position
    Z  = Point(float(sys.argv[1]), float(sys.argv[2]))

    Pz = NN.get(Z)

    import skimage
    import skimage.io

    img = skimage.io.imread('./movingDetect/result.jpg');
    a = img[Pz.x, Pz.y]

    import json
    print(json.dumps({'x': Pz.x, 'y': Pz.y, 'value': int(a[0])}))
