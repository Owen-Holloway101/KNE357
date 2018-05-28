import point

class path:
    points = []

    def __init__(self):
        self.points = []

    def addPoint(self, point):
        self.points.append(point)

    def printPath(self):
        print("Path Start")
        print("--->")
        for p in self.points:
            p.printPoint()
            print("--->")
        print("Path End")
