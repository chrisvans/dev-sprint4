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

