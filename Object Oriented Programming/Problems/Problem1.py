#A PROGRAM THAT CREATES A LINE CLASS THAT CAN CALCULATE DISTANCE AND SLOPE
import math
class Line:

    def __init__(self,coor1,coor2):
        #takes in coordinates
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        #returns the distance a^2 + b^2 = c^2
        totalx = self.coor2[0] - self.coor1[0]
        totaly = self.coor2[1] - self.coor1[1]
        total_dist = ((totalx**2) + (totaly**2))
        total_dist = math.sqrt(total_dist)
        return total_dist

    def slope(self):
        #returns the slope (y2-y1)/(x2-x1)
        totalx = self.coor2[0] - self.coor1[0]
        totaly = self.coor2[1] - self.coor1[1]
        slope = totaly/totalx
        return slope

coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())
