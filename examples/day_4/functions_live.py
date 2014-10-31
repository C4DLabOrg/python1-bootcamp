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

print("\n\n\nStuff after hackathon >>>\n\n\n")

'''
Post-hackathon refinements:
Folks, time flies, lots of stuff we didn't handle.
If you followed our example above, we wish to
refine this function into proper function(s)

We want to have one function that counts 
election votes and rigs (conditionally)

First, let's start with better data structures.
We want to store the name of the candidates,
and the polling stations with their respective
tallies:
	* I'll use a list of dictionaries!
	* Remember our country has got 7 counties:
		- Tharaga Nithi
		- Pungoma
		- Nairopi
		- Naguru
		- Napythoni
		- Kizumu
		- Gost
	So we can simply store the votes as a list
	rather than a dictionary within a dictionary
	(though this way too is fine)
	* We have a key in each dictionary called 'total'
		for displaying the tallied totals, initialized
		with None, before the votes are counted
'''
counties = ['Tharaga Nithi', 'Pungoma', 'Nairopi',
			'Naguru', 'Napythoni', 'Kizumu', 'Gost']

tallies = [
	{
		'name': 'Pifwol Wakol',
		'total': None,
		#rather than >> 
		#'votes' : {
		# 	'Tharaka Nithi' : 0,
		# 	'Bungoma' : 400,
		# 	'Nairopi' : 50,
		# 	'Naguru' : 80,
		# 	'Napythoni' : 30,
		# 	'Kizumu': 300,
		# 	'Bwani' : 75
		# } #use below instead
		'votes' : [0,400,50,80,30,300,75]
	},
	{
		'name' : 'Ohuru Odinga',
		'total': None,
		'votes' : [1000,30,10,80,40,70,50]
	},
	{
		'name' : 'Raira Genyatta',
		'winner' : None,
		'votes' : [10,300,80,80,30,600,100]
	},
	{
		'name' : 'Muzalia Mtaf',
		'total' : None,
		'votes' : [1,5,10,200,50,90,75]
	},
	{
		'name' : 'Nimuite Muite',
		'total' : None,
		'votes' : [5,3,10,16,19,50,12]
	}
]

#We could get totals for each candidate by simply
#sum(tallies[candidate_index]['votes'])
#e.g. for Pifwoli Wakoli

pif_totals = sum(tallies[0]['votes'])
print("{0} has {1} votes".format(tallies[0]['name'],pif_totals))

#But remember we wish to write our own `sum` function
#so that we learn!
#and also have another flawed implementation of it that rigs

#So let's call it count_votes
#You only give it (1) the list of votes and 
#(2) the rigging factor (rf) - the additional fraudilent votes that
#will be added over and above the real votes.

def count_votes(votes,rf=0):
	#get total, we will not use BIF sum()!
	total = 0
	for i in votes:
		total = total + i

	#when done, add the rigging factor (rf)
	total = total + rf
	return total

#Let's apply the function to our data, storing the totals
#in the total key

for i in tallies:
	if i['name'] == 'Ohuru Odinga':
		total = count_votes(i['votes'],300)
	else:
		total = count_votes(i['votes'])
	
	i['total'] = total

#print to see if the totals have been done
print(tallies)

#next is declaring the winner
#let's find the person with the highest votes

winner = None
highest = 0

for i in tallies:
	if i['total'] > highest:
		highest = i['total']
		winner = i['name']

#Hazzan, declare ther winner!
print("\n----drums roll----\n")

print("And the winner is {0} with {1} votes".format(winner,highest))
print("\n----end of elections, tyranny of numbers! :)----\n")


'''
Hope the above example made sense.
Folks, ping us if you got any questions, 
we wish you happy coding :)

Hope you "is liking" the Python ;)

Signed - @profnandaa
Thanks to my TAs - @shimanyi and @alexanderMwangi
End of Bootcamp
'''