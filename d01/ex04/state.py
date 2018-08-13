import sys

def state_name(capital):
	states = {
  		"Oregon"    : "OR",
		"Alabama"   : "AL",
		"New Jersey": "NJ",
		"Colorado"  : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	# for city in capital_cities:
	# 	if capital_cities[city] == capital:
	# 		for state in states:
	# 			if city == states[state]:
	# 				print (state)
					
	# if capital_cities[capital] in capital_cities:
	# 	print (capital_cities[capital])
		# for state in states:
		# 	if capital_cities[city] == states[state]:
		# 		print (state)
	# else:
		# print ('Unknown capital city')
	# print (capital_cities[capital] )
	# if capital_cities[capital] in capital_cities:
	# 	print (states[])
	# else:
		# print ('Unknown capital city')

if __name__ == '__main__':
	if len(sys.argv) == 2:
		state_name(sys.argv[1])