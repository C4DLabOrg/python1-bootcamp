#!/usr/bin/python
# Filename: break.py

while True:
	s = raw_input('Enter something : ')
	if s == 'quit':
		break
	print('Length of the string is {0}'.format(len(s)))
print('Done')

