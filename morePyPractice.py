import sys, random, json, re, math, string
from datetime import datetime

def char_input():
	name =  raw_input("Enter your name: ")
	print "your name is "+name
	age = input("Enter your age: ")
	currentYear = datetime.now().year
	#print currentYear
	print name+", you will turn 100 years old in the year "+str(100-age+currentYear)+"."

	otherNumber = input("Give me another number: ")
	for i in range(0, otherNumber):
		print name + " you will turn 100 years old in the year "+str(100-age+currentYear)+"."

def odd_or_even():
	number = input("Give me a number: ")
	#print number % 2
	if number % 4 == 0:
		print "number is a multiple of 4."
	elif number % 2 == 0:
		print "number is even."
	else:
		print "number is odd."
	
	num = input("Give me another number: ")
	check = input("Give me a divisor: ")
	if num % check == 0:
		print str(check)+" divides evenly into "+str(num)+"." 
	else:
		print str(check)+" does not divide evenly into "+str(num)+"." 

def list_lt_10(a):
	b = []
	for x in a:
		if x < 5:
			#print a[i]
			b.append(x)
	print b

	##THIS IS HOW TO DO IT IN ONE LINE; CALLED LIST COMPREHENSION
	b = [x for x in a if x<5]
	print b

	comparator = input("Give me a number: ")
	b = [x for x in a if x<comparator]
	print "elements of a that are less than "+str(comparator)+":"
	print b

def divisors():	
	num = input("Give me a number: ")
	print "Divisors for "+str(num)+":"
	a = []
	for x in range(1, num/2+1):
		if num % x == 0:
			a.append(x)
	#print a
	for elem in a:
		print elem

def list_overlap(a,b):	
	#The command ast.literal_eval(string) converts string argument to list
	#a = ast.literal_eval(sys.argv[1])
	#b = ast.literal_eval(sys.argv[2])

	print "a="+str(a)
	print "b="+str(b)
	c = []
	
	#for x in a:
		#print x
	#	if x in a and x in b and x not in c:
	#		c.append(x)

	#do the LIST COMPREHENSION to get common values for a and b
	[c.append(x) for x in a if x in b and x not in c]
	
	print c
	
def is_palindrome(s):
	for i in range(0,len(s)):
		if s[i] != s[len(s)-1-i]:
			return False
	return True
	
def only_even(a):
	b = [x for x in a if x%2 == 0]
	return b

def rps_play():
		valid_play = "[RPSrps]"
		play = raw_input("enter your play (R/P/S): ")
		while (not re.match(valid_play, play)):
			play = raw_input("Invalid play. Try again: ")
		return play
						
def rock_paper_scissors():
	p1 = ""
	p2 = ""
	while p1.lower() == p2.lower():
		print "Player 1",
		p1 = rps_play()
		print "Player 2",
		p2 = rps_play()
		
	if (p1.lower() == "r" and p2.lower() == "s"
		or p1.lower == "p" and p2.lower() == "r"
		or p1.lower() == "s" and p2.lower() == "p"):
		print "Player 1 wins!"
	else:
		print "Player 2 wins!"
		
def guessing_game():
	guess = 0
	new_game = ""
	
	num = random.randint(1,9)
	num_guesses = 0
	while guess != num:
		guess = input("Guess a number between 1 and 9: ")
		num_guesses += 1
		if guess < num:
			print "Too low! Guess again."
		elif guess > num:
			print "Too high! Guess again."
		else:
			print "Correct! That only took "+str(num_guesses)+" guesses!"
			num_guesses = 0
			new_game = raw_input("Play again? (type 'exit' to quit) ")
			if new_game != "exit":
				num = random.randint(1,9)
				guess = 0
			else:
				break

def list_overlap(a, b):
	c = []
	[c.append(x) for x in a if x in b and x not in c]
	return c
	
def is_prime(x):
	for i in range(2, int(math.sqrt(x)+1)):
		if x % i == 0:
			return False
	return True
	
def list_ends(a):
	return [a[0], a[-1]] #the -1 index signifies the last index of the list

def fibonacci():
	amount = input("How many Fibonacci numbers? ")
	fib_list = []
	print "The first " + str(amount) + " Fibonacci numbers are:"
	
	for i in range(0, amount):
		if i <= 1:
			fib_list.append(1)
		else:
			fib_list.append(fib_list[i-1] + fib_list[i-2])
		print str(fib_list[i]) + " ",
	print ""
	
def list_remove_duplicates(a):
	a = set(a)
	return list(a)
	
def reverse_word_order(s):
	return " ".join(reversed(s.split()))
	
def password_generator():
	char_set = string.ascii_uppercase + string.ascii_lowercase + string.digits
	num_chars = input("How long do you want your password to be? ")
	return "".join(random.sample(char_set, num_chars))
	
def binary_search(x, a):
	start = 0
	end = len(a)-1
	
	while start <= end:
		mid = (start + end)/2
		print "searching on index "+str(mid)
		if a[mid] == x:
			return True
		elif x < a[mid]:
			end = mid - 1
		elif x > a[mid]:
			start = mid + 1
	return False
	
def read_from_file(f):
	name_counts = {}
	open_file = open(f, "r")
	for line in open_file:
		line = line.strip()
		if line not in name_counts.keys():
			name_counts[line] = 0
		name_counts[line] += 1
	
	for name in name_counts.keys():
		print name + ": " + str(name_counts[name])

def put_lines_in_list(f):
	open_file = open(f, "r")
	f_list = []
	
	for line in open_file:
		f_list.append(int(line))
		
	return f_list
		
def file_overlap(f1, f2):
	f1_list = put_lines_in_list(f1)
	f2_list = put_lines_in_list(f2)
	
	return [x for x in f1_list if x in f2_list]
		
	
def main():
	#char_input()
	#odd_or_even()
	a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	#a = [1, 1, 2, 4, 2, 3, 5, 7, 4, 3, 4, 6, 8, 10, 12, 8, 10]
	#list_lt_10(a)
	#divisors()
	
	#Code to RANDOMLY GENERATE lists using random module
	#xrange(x,y) means range of values within list, second number is number
	#of items in list (in this case, a randomly generated integer)
	#a = random.sample(xrange(1,101),random.randint(1,10))
	#b = random.sample(xrange(1,101),random.randint(1,10))
	print a
	#print b
	
	#list_overlap(a,b)
	#print is_palindrome(sys.argv[1])
	#b = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
	#print only_even(b)
	#rock_paper_scissors()
	#guessing_game()
	#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	#print list_overlap(a, b)
	print is_prime(53)
	print list_ends(a)
	#fibonacci()
	print list_remove_duplicates(a)
	print reverse_word_order("My name is Arjun")
	#print password_generator()
	print binary_search(4, a)
	read_from_file("nameslist.txt")
	print file_overlap("primenumbers.txt", "happynumbers.txt")
	
	
if __name__ == "__main__":
	main()
