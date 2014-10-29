#!/usr/bin/python
# Filename: using_tuple.py
zoo = ('python', 'elephant', 'penguin') # remember the parentheses are optional
print('Number of animals in the zoo is {0}'.format(len(zoo)))
new_zoo = ('monkey', 'camel', zoo)
print('Number of cages in the new zoo is {0}'.format(len(new_zoo)))
print('All animals in new zoo are {0}'.format(new_zoo))
print('Animals brought from old zoo are {0}'.format(new_zoo[2]))
print('Last animal brought from old zoo is {0}'.format(new_zoo[2][2]))
print('Number of animals in the new zoo is {0}'.format(
len(new_zoo)-1+len(new_zoo[2])))


#singleton tuple, e.g

extinct = ('dinosaur',)		#you have to add the extra comma

