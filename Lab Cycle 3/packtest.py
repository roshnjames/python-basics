from packs import circle
from packs import rectangle
from packs import*
from packs.graphics import spheres
from packs.graphics import cuboids

print("Circle")
r=int(input("Enter the radius of the circle: "))
circle.circle(r)
print()

print("Rectangle")
l=int(input("Enter the length of the rectangle: "))
b=int(input("Enter the breadth of the rectangle: "))
rectangle.rect(l,b)
print()

print("Sphere")
spheres.sphere()
print()

print("Cuboid")
cuboids.cuboid()
print()
