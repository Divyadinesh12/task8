class circle():
     def __init__(self,r):
          self.radius=r
#area formula in cicle 22/7 r*2
     def area(self):
          return(3.14*(self.radius**2))
#perimeter formula in circle 2*22/7*r 
     def perimeter(self):
          print(2*3.14*self.radius)
newcircle=circle(8)
print(newcircle.area())
newcircle.perimeter()