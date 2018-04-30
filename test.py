from point import point
from path import path

point1 = point(1,2,3,4)
point2 = point(2,2,3,4)
point3 = point(3,2,3,4)
point4 = point(4,2,3,4)
point5 = point(5,2,3,4)
point6 = point(6,2,3,4)

path1 = path()
path1.addPoint(point1)
path1.addPoint(point2)
path1.addPoint(point3)
path1.addPoint(point4)
path1.addPoint(point5)
path1.addPoint(point6)

path1.printPath()
