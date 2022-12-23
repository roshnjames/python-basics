class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        a=self.l*self.b
        return a
    def peri(self):
        p=2*(self.l+self.b)
        return p

ob1=Rectangle(2,3)
ob2=Rectangle(4,5)
ar1 = ob1.area()
p1 = ob1.peri()

ar2 = ob2.area()
p2 = ob2.peri()

print("Area of 1st rectangle : ",ar1)
print("Area of 2nd rectangle : ",ar2)
if(ar1>ar2):
      print("Rectangle 1 is larger")
else:
      print("Rectangle 2 is larger")
             
