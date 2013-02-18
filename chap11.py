# Name: Chris Van Schyndel

# Exercise 11.8
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
	global workaround
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
# will return none.

#def modular_multiplicative(number, modulard, multiple=1):
#	global workaround
#	tryone = (modulard * multiple)
#	trytwo = ((tryone * 1.0 + 1) % number)
#	if trytwo == 0:
#		workaround = ((tryone * 1.0) + 1) / number
#	else:
#		modular_multiplicative(number, modulard, multiple+1)

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

