names = [
	'Mike','John','Kivisi',
	'Wanyonyi','Rapando','Shimanyi',
	'Kelvin','Kamau','Lude',
	'Lutta','Emmanuel',"O'neal"
]
# names.sort()

most_wanted = ['Mike','Lutta','Lude']

#We want to arrest the culprits
for name in names:
	if name in most_wanted:
		print("Arrest " + name)

#Let's refine our solution
caught = 0

for name in names:
	if name in most_wanted:
		print("Arrest " + name)
		caught = caught + 1
		if caught == len(most_wanted):
			break


#let's do loops
# count = 0
# for name in names:
# 	count = count + 1
# 	print(str(count) + ". " + name)
