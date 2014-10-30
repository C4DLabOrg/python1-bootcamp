#Let's do our own sum() that can be
#used for rigging elections!

votes = [100,20,40,10,0]

def sum_rigged():
	total = 0
	for i in votes:
		total = total + i
	#loop is over
	#rig!
	total = total + 10
	return total

#call
votes = sum_rigged()

print("The winner is Dida \
with {0} votes!".format(votes))
