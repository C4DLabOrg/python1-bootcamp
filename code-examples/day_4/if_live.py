student1 = {
	'name' : 'Sheila',
	'class' : 8,
	'age': 90
}

student2 = {
	'name':'John',
	'class':4,
	'age':10
}

if student1['age'] < 12:
	print("Repeat class 8")
elif student1['age'] <= 14:
	print("Proceed to F1")
else:
	print("Too old to be admitted")
