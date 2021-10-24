class Point():
    def __init__(self):
        x = int(input('x is '))
        y = int(input('y is '))
        self.x = x
        self.y = y

class Shape(object):
    def area(self):
        pass
    def perimeter(self):
        pass
    
class Rectangle(Shape):
    def __init__(self):
        lst = list()
        lst1 = list()
        for i in range(4):
            points = Point()
            lst.append(points)
        i, j = 0, 0
        s1, s2 = 0, 0
        for i in range(4):
            for j in range(4):
                if i != j:
                    lst1.append([(lst[i].x - lst[j].x), (lst[i].y - lst[j].y)])
        for i in range(len(lst1)):
            for j in range(len(lst1)):
                if (lst1[i][0]*lst1[j][0] + lst1[i][1]*lst1[j][1]) == 0:
                    s1 = (lst1[i][0]**2 + lst1[i][1]**2)**0.5
                    s2 = (lst1[j][0]**2 + lst1[j][1]**2)**0.5
                    break
        
        self.side1 = s1
        self.side2 = s2

    def area(self):
        return self.side1*self.side2
    def perimeter(self):
        return 2*self.side1 + 2*self.side2
    
class Square(Rectangle):
    def area(self):
        return self.side1*self.side1
    def perimeter(self):
        return 4*self.side1
rect = Rectangle()
print("  Area: " + str(rect.area()))
print("  Perimeter: " + str(rect.perimeter()))
