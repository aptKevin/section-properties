import numpy as np


def RotateXYcoord(xyCoordList, angle):
    '''
    Rotate the x,y coord list by angle(degree) in counter clock direction
    :param xyCoordList: [(x,y),(x2,y2),...]
    :param angle : float unit degree
    :return newxylist
    '''
    newxyList = []
    for (x, y) in xyCoordList:
        alpha = np.radians(angle)
        x0 = x * np.cos(alpha) - y * np.sin(alpha)
        y0 = x * np.sin(alpha) + y * np.cos(alpha)
        newxyList.append((x0, y0))

    return newxyList


xyList = [(1, 2), (2, 3), (3, 4), (5, 6)]

xyList = RotateXYcoord(xyList, 50)

print(xyList)
