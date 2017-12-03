"""this file defines an itertool 
that can generate infinite letter-num 
sequences like a1,b1,c1...zi,a2,b2..."""

def alphabet_num_cycle():
	i = 1
	while True:
		for letter in "abcdefghijklmnopqrstuvwxyz".lower():
			yield letter + str(i)
		i += 1
		
k = 0
for letter in alphabet_num_cycle():
	print letter
	# these lines used to test programme
	k += 1
	if k > 100:
		break