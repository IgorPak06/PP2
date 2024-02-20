import math

side = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))

a = (1/4) * side * math.pow(l, 2) * (1 / math.tan(math.pi / side))

print("The area of the polygon is: ", math.trunc(a))