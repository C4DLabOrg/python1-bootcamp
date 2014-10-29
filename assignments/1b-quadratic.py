import math

#Quad formula: x*x + 5x + 3 = 0

a = 1
b = 5
c = 3

x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)

x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)

print("x1 is {0} and x2 is {1}".format(x1,x2))

#we can make it look nice, round it off
print("x1 is {0} and x2 is {1}".
	format(round(x1,3),round(x2,3)))
