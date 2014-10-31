'''
We want to explore (the beauty of) Python here, just a little bit.
'''

'''
(1) Dynamic typing - our variable can change type anytime
See Further Reading section for reading material on Static vs. Dynamic typing
'''
name = "Nandaa" 	#here name is a string
print(name * 3)

name = 30			#here name is an integer
print(name * 3)

name = str(name)	#here name is type-casted to a string from integer
print(name * 3)

'''
(2) Dynamic typing can be source of bug too! 
Remember our class example?
Area of a triangle = 1/2 * b * h
'''

b = 30
h = 10
area = 1/2 * b * h 		#Area = 0! why? Because 1/2 = 0 in 
						#Python (integer division).

print("The area is " + str(area))

area = 1.0/2 * b * h 	#Correct implementation

print("The area is " + str(area))

'''
(3) Readability of code (almost like English!)
Example:
'''
x = 10

if x is not 4:
	print("It's not 4!")
else:
	print("Ok, got it!")

#However, we will do If..Else, etc on Day 3, so don't panic :)

'''
(4) Using dir() function to explore various objects in Python
Remember: Everything in Python is an object!

Example
'''

#print(dir(name))
#print(dir(age))

'''
(5) Other things in Python

* Logical vs. physical lines of code
* Semi-colons (;) are not necessary in Python!
* You should be in love with the language by now :)

'''

'''
(6) Multiple initialization

e.g:
'''

name, age, nationality = "James", 45, "Kenyan"

print("{0} is {1} years old, and is {2}".format(name,age,nationality))



