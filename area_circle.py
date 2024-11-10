def AreaofCircle():
    r=int(input("Enter The Radius: "))
    pi=3.14
    area=pi*r*r
    circum=2*pi*r  
    print(f"Area of Circle: {area}")
    print(f"Circumference of Circle: {circum:.2f}")

AreaofCircle()