import math
class Shape:
    def __init__(self):
        self
    def area(self):
        raise NotImplementedError
class Rectangle(Shape):
           def __init__(self, length, width ):
                 super().__init__()
                 self.length=length
                 self.width=width
           def area(self):
                result = self.length * self.width
                return result
class Circle(Shape):
      def __init__(self, radius):
            super().__init__()   
            self.radius = radius 
      def area(self):
            r1 = math.pi * pow(self.radius, 2)
            return r1         


