
#generating a list
my_list = range(20)

#find length of string
len(my_list)

#access an item in the list
print(my_list[3])

#append to list

my_list.append(21)

print(my_list)

#delete from list
del my_list[0]

print(my_list)

#nested list - list within a list
my_list.append(range(5))

print(my_list)

#sorting a list

langs = ['C++','Java','Perl','Python','Ada','JavaScript','Rust','C#']

good_langs = ['C++','JavaScript','Python']

print(langs)
langs.sort()
print(langs)

#Iterating over list, using loops (in the next session, but let's try)

#simply printing the list

for i in langs:
	print i


#a little more than print

for i in langs:
	if i is 'Python':
		print i + " - the best language"
	elif i in good_langs:
		print i + " - a good language"
	else:
		print i



#List comprehensions - provide a concise way to create lists. 
comp_list = [x**2 for x in range(10)]

print(comp_list)