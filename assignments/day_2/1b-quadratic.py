import math

#Quad formula: x*x + 5x + 3 = 0
#use input() for Python v.3.x
print("Given a quadratic equation, ax2+bx+c = 0")
a = raw_input("Give a: ")
b = raw_input("Give b: ")
c = raw_input("Give c: ")

x1 = (-b + math.sqrt(b*b - 4*a*c))/(2.0*a)

x2 = (-b - math.sqrt(b*b - 4*a*c))/(2.0*a)

print("x1 is {0} and x2 is {1}".format(x1,x2))

#we can make it look nice, round it off
print("x1 is {0} and x2 is {1}".
	format(round(x1,3),round(x2,3)))
