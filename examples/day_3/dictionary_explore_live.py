#simple dictionary

student1 = {
	'name' : 'Tracy',
	'age' : 25,
	'nationality' : 'Ugandan'
}

print("{0} is {1}".format(student1['name'],
					student1['nationality']))


#complex dictionary
student2 = {
	'name' : 'Joseph N.',
	'year' : '1st',
	'uni' : 'University of Nairobi',
	'langs' : ['Python','Android','HTML',
				'Java','English','Swahili','Kikuyu'],
	'phone' : {
		'make' : 'Blackberry',
		'year_bought' : '2013',
		'price' : 450.00,
		'OS' : 'Blackberry',
		'city' : 'Nairobi'
	}
}

print("{0} owns a {1}".format(student2['name'],
	student2['phone']['make']))

# print(dir(student1))
