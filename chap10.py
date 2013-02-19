# Name: Chris Van Schyndel

# Exercise 10.4

def middle(some_list):
	some_list.pop(0)
	some_list.pop(len(some_list)-1)
	return some_list

a_list = ['bagels', 'cheesecake', 'necromancer', 'cellular', 'lagomorph']
a_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a_list3 = [5, 2, 1, 6464, [12693, 84573]]
print middle(a_list), middle(a_list2), middle(a_list3)


# Exercise 10.10

def appendor():
	bagel = []
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		#bagel.append(word)
		bagel = bagel + [word]
	return bagel


# Exercise 10.7

def is_anagram(stringone, stringtwo):
	# This function takes two strings and returns True or False relative
	# to whether or not they are anagrams of each other.
	comparedictone = {}
	comparedicttwo = {}
	# Initialize dictionaries and standardize strings to lower case for comparison
	stringone = stringone.lower()
	stringtwo = stringtwo.lower()
	# Populate dictionaries, if a letter exists, add to it's count value, if not, add it
	# initially with a count value of 1.
	for letter in stringone:
		if letter in comparedictone:
			comparedictone[letter] = comparedictone[letter] + 1
		else:
			comparedictone[letter] = 1
	for letter in stringtwo:
		if letter in comparedicttwo:
			comparedicttwo[letter] = comparedicttwo[letter] + 1
		else:
			comparedicttwo[letter] = 1
	# Remove empty spaces from dictionaries, as they do not matter for comparison.
	if ' ' in comparedictone:
		del comparedictone[' ']
	if ' ' in comparedicttwo:
		del comparedicttwo[' ']
	# Compare dictionaries, if all keys and values match, then they are anagrams.
	return comparedictone == comparedicttwo

print is_anagram('rartec', 'carter')
print is_anagram('cello', 'jello')
print is_anagram('Astronomers', 'No more stars')

# Exercise 10.13

# Misunderstood question here.

#def interlocked_word(stringone, stringtwo):
#	baglace = open('words.txt')
#	interlock_list = []
#	for line in baglace:
#		word = line.strip()
#		if is_anagram(stringone + stringtwo, word):
#			interlock_list.append(word)
#	return interlock_list
#
#print interlocked_word('shoe', 'cold')

def interlocked_word(stringone, stringtwo):
	# Expects two strings of the same length, otherwise returns False
	# Returns the interlocked string, regardless of whether or not it is a valid word.
	if len(stringone) != len(stringtwo):
		return False
	possibleinterlock = ''
	for indexor in range(len(stringone)*2):
		if indexor == 0:
			possibleinterlock += stringone[0]
		elif indexor == 1:
			possibleinterlock += stringtwo[0]
		elif indexor % 2 == 0:
			possibleinterlock += stringone[indexor/2]
		else:
			possibleinterlock += stringtwo[indexor/2]
	return possibleinterlock

print interlocked_word('shoe', 'cold')
	

