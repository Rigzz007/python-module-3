'''
1)write a python program to convert degree to radian
2)write a python program to calculate the area of a trapezoid
3)write a python program to calculate the area of a parallelogram
4)write a python program to calculate surface volume and area of a cylinder
'''
#1)

pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)

#2)

base_1 = 5
base_2 = 6
height = float(input("Height of trapezoid: "))
base_1 = float(input('Base one value: '))
base_2 = float(input('Base two value: '))
area = ((base_1 + base_2) / 2) * height
print("Area is:", area)

#3)

base = float(input('Length of base: '))
height = float(input('Measurement of height: '))
area = base * height
print("Area is: ", area)

#4)

pi=22/7
height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))
volume = pi * radian * radian * height
sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)
print("Volume is: ", volume)
print("Surface Area is: ", sur_area)
