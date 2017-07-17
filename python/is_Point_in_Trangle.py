# Given the 3 points to repesent a 2D triangle, and a point.
# Check whether the point is inside the triangle, including the edge.

import random

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __cmp__(self, other):
        return (self.x - other.x, self.y - other.y)

    def __str__(self):
        return "[%f, %f]" % (self.x, self.y)


def getVector(v1, v2):
    return Point(v2.x - v1.x, v2.y - v1.y)

def calculateTriangleArea(v1, v2, v3):
    vector1 = getVector(v1, v2)
    vector2 = getVector(v1, v3)
    return abs(vector1.x * vector2.y - vector2.x * vector1.y) / 2.0

def isInTriangle_AreaSolution(v1, v2, v3, point):
    triangleArea = calculateTriangleArea(v1, v2, v3)
    area1 = calculateTriangleArea(v1, v2, point)
    area2 = calculateTriangleArea(v2, v3, point)
    area3 = calculateTriangleArea(v3, v1, point)
    # print area1 + area2 + area3, triangleArea , 11
    return area1 + area2 + area3 == triangleArea

def crossProduct(vector1, vector2):
    return vector1.x * vector2.y - vector2.x * vector1.y

def isInTriangle_PositionSolution(v1, v2, v3, point):
    side1 = crossProduct(getVector(v1, v2), getVector(v1, point))
    side2 = crossProduct(getVector(v2, v3), getVector(v2, point))
    side3 = crossProduct(getVector(v3, v1), getVector(v3, point))
    # print side1,side2,side3,22,
    positive = side1>=0 and side2>=0 and side3>=0
    negative = side1<=0 and side2<=0 and side3<=0
    # print positive, negative
    return positive or negative


# test functions
def PointGenerator(lower, higher):
    randNum = random.randrange
    return Point(randNum(lower, higher), randNum(lower, higher))

def pointOnLine(v1, v2):
    if v1.x == v2.x:
        return
    minX = min(v1.x, v2.x)
    maxX = max(v1.x, v2.x)
    for x in xrange(minX, maxX):
        res, rem = divmod(v2.y - v1.y, v2.x - v1.x)
        if rem == 0:
            y = v1.y + res * (x - v1.x)
            yield Point(x, y)


def randomTest():
    times = 1000
    lower = -20
    higher = 20
    for i in xrange(times):
        v1 = PointGenerator(lower, higher)
        v2 = PointGenerator(lower, higher)
        v3 = PointGenerator(lower, higher)
        point = PointGenerator(lower, higher)
        ans1 = isInTriangle_PositionSolution(v1, v2, v3, point)
        ans2 = isInTriangle_AreaSolution(v1, v2, v3, point)
        assert ans1 == ans2
        # if ans1 != ans2:
        #     print v1, v2, v3, point, ans1, ans2

def onEdgeTest():
    times = 1000
    lower = -20
    higher = 20
    for i in xrange(times):
        v1 = PointGenerator(lower, higher)
        v2 = PointGenerator(lower, higher)
        v3 = PointGenerator(lower, higher)
        # cnt = 0
        for point in pointOnLine(v1, v2):
            # if not isInTriangle_PositionSolution(v1, v2, v3, point):
            #     print v1, v2, v3, 1
            # if not isInTriangle_AreaSolution(v1, v2, v3, point):
            #     print v1, v2, v3, 2
            # cnt += 1
            assert isInTriangle_PositionSolution(v1, v2, v3, point) == True
            assert isInTriangle_AreaSolution(v1, v2, v3, point) == True
        for point in pointOnLine(v2, v3):
            # cnt += 1
            assert isInTriangle_PositionSolution(v1, v2, v3, point) == True
            assert isInTriangle_AreaSolution(v1, v2, v3, point) == True
        for point in pointOnLine(v3, v1):
            # cnt += 1
            assert isInTriangle_PositionSolution(v1, v2, v3, point) == True
            assert isInTriangle_AreaSolution(v1, v2, v3, point) == True
        # print cnt

if __name__ == '__main__':
    randomTest()
    onEdgeTest()
    # v1 = Point(-1, -14)
    # v2 = Point(-19, -2)
    # v3 = Point(10, 17)
    # point = Point(-5, -4)
    # print isInTriangle_AreaSolution(v1, v2, v3, point)
    # print isInTriangle_PositionSolution(v1, v2, v3, point)
    

