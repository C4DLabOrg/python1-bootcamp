#!/usr/bin/python
# Filename: str_format.py

age = 25
name = 'Swaroop'
print('{0} is {1} years old'.format(name, age))
#another way of putting doing line 6
print(name + " is " + str(age) + " years old")

print('Why is {0} playing with that python?'.format(name))

print('{name} wrote {book}'.format(name='Swaroop',
book='A Byte of Python'))


