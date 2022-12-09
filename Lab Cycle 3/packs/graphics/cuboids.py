def cuboid():
    l=int(input("Enter length"))
    b=int(input("Enter breadth"))
    h=int(input("Enter height"))
    area=2*((l*b)+(b*h)+(h*l))
    peri=4*(l+b+h)
    print("Total surface area of the cuboid is: ",area)
    print("Perimeter of the cuboid is: ",peri)
