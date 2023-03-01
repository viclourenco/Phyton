import math

def compute_area_square(side):
    return side * side

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius

shape = ""
while shape != quit:
  shape = input("Choose a shape: \n1- Rectangle \n2- Circle \n3- Square \n")

  if shape == "1":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area = compute_area_rectangle(length, width)
        print(f"The area is {area}")

  if shape == "2":
        radius = float(input("What is the radius? "))
        area = compute_area_circle(radius)
        print(f"The area is {area}")
      
  if shape == "3":
        side = float(input("What is the length of the side? "))
        area = compute_area_square(side)
        print(f"The area is {area}")

print (" ")
print ("See you later")

