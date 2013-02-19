# Name: Chris Van Schyndel

# Exercise 11.8
# Why did I do exercise 11.8?  Uhh...  I dunno.
import random
import fractions

# Write functions to encode and decode messages
def prime_number(number):
	count = 0
	for numbers in range(number):
		bagel = number % (numbers + 1)
		if bagel == 0:
			count += 1
	if count == 2:
		return True
	else:
		return False

def a_prime():
	while True:
		numberone = random.randint(0, 100)
		if prime_number(numberone):
			return numberone

def key_generation():
	prime1 = a_prime()
	prime2 = a_prime()
	key_length = prime1 * prime2
	computetotient1 = eulers_totient(key_length)
	computetotient2 = (prime1 - 1) * (prime2 - 1)
	chosen_one = choose_coprime_int(computetotient2)
	privated = modular_multiplicative(chosen_one, computetotient1)
	public_key = (key_length, chosen_one)
	private_key = (key_length, privated)
	return public_key, private_key

# For a padded plaintext message m:
# m**chosen_one ( mod key_length)
# For an encrypted ciphertext c:
# c**privated ( mod key_length)



# Strange issues here, if I put a return statement after the if,
# I get 'None'.  I had to make a global variable workaround in order to
# store the modular multiplicative inverse.  I can put a print statement
# before the return statement that contains the exact same calculation,
# the print statement will return the correct number, while the function
# will return none.  The previous calls to the function also do not return 
# anything. It seems recursion takes up far more memory
# than a while loop anyways, and so I opted to use While to avoid
# recursion depth errors.

#def modular_multiplicative(number, modulard, multiple=1):
#	global workaround
#	tryone = (modulard * multiple)
#	trytwo = ((tryone * 1.0 + 1) % number)
#	if trytwo == 0:
#		print ((tryone * 1.0) + 1) / number
#		workaround = ((tryone * 1.0) + 1) / number
#		return ((tryone * 1.0) + 1) / number
#	else:
#		modular_multiplicative(number, modulard, multiple+1)
#	return 'Past calls'

def modular_multiplicative(number, modulard):
	multiple = 1
	while True:
		tryone = (modulard * multiple)
		trytwo = ((tryone * 1.0 + 1) % number)
		if trytwo == 0:
			break
		multiple += 1
	return int((((tryone * 1.0) + 1) / number))


def choose_coprime_int(key_length):
	while True:
		numbertwo = random.randint(0, 100)
		if 1 < numbertwo < eulers_totient(key_length) and fractions.gcd(numbertwo, eulers_totient(key_length)) == 1:
			return numbertwo

def eulers_totient(n):
	count = 0
	for number in range(n):
		if prime_number(number+1):
			count += 1
	return count

def find_closest_prime(number):
    numberchange = 0
    changer = False
    numbered = number
    closecheck = 0
    while True:
        if changer and numberchange != 0:
            closecheck = number - numberchange
        elif numberchange != 0:
            closecheck = number + numberchange
        if prime_number(numbered):
            if prime_number(numbered) and prime_number(closecheck):
                return numbered, closecheck
            else:
                return numbered
        else:
            numberchange += 1
            changer = not changer
            numbered = crement(number, numberchange, changer)
            
def crement(number, summer, change):
    if change:
        return number + summer
    else:
        return number - summer


print key_generation()

# Exercise 11.9

def has_duplicates(zelist):
	ledict = {}
	for element in range(len(zelist)):
		if zelist[element] in ledict:
			return True
		else:
			ledict[(zelist[element])] = zelist[element]
	return False

print has_duplicates([1, 2, '11', '1', 7, '3', 5])

# Exercise 11.10

def rot_x(astring, rotator):
	alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
	newstring = ''
	for letter in astring:
		if letter in alpha_upper:
			newletter = alpha_upper[(alpha_upper.find(letter) + rotator) % 26]
			newstring += newletter
		if letter in alpha_lower:
			newletter = alpha_lower[(alpha_lower.find(letter) + rotator) % 26]
			newstring += newletter
	return newstring

def rotate_pairs(wordlist):
	rotatepairs = []
	for word in wordlist:
		for rotator in range(25):
			if rot_x(word, rotator) in wordlist and rot_x(word, rotator) not in rotatepairs and rotator != 0:
				rotatepairs.append(word)
				rotatepairs.append(rot_x(word, rotator))
		for backrotator in range(25):
			backrotator = - backrotator
			if rot_x(word, backrotator) in wordlist and rot_x(word, backrotator) not in rotatepairs and backrotator != 0:
				rotatepairs.append(word)
				rotatepairs.append(rot_x(word, backrotator))
	pairedpairs = []
	index = 0
	for pair in rotatepairs:
		if index == 0 or (index % 2) == 0:
			print index
			pairedpairs.append([pair, rotatepairs[index+1]])
		index += 1
	return pairedpairs

print rotate_pairs(['apple', 'barnacle', 'alfalfa', 'melon', 'cheer', 'jolly', 'cubed'])