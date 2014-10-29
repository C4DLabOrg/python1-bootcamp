import math

#use input() for v. 3.x

a = int(raw_input("Give a: ")) #type-cast
b = int(raw_input("Give b: "))

#hypotunuse
h = math.sqrt(a*a + b*b)

print("Hypotunuse is {0}".format(round(h,2)))
