#!/usr/bin/python
# Filename: func_param.py

def printMax(a, b):
	if a > b:
		print(a, 'is maximum')
	elif a == b:
		print(a, 'is equal to', b)
	else:
		print(b, 'is maximum')

printMax(3, 4) # directly give literal values
x = 5
y = 7

printMax(x, y) # give variables as arguments

