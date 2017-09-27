import sys, random, json
from collections import Counter
from bokeh.plotting import figure, show, output_file

def who_won_ttt(list_a):
	#find 3 in a row horizontal, vertical, or diagonal for either Player 1 or Player 2
	#first find horizontal with identical entries (non-zero)
	winner_found = False
	
	for row in range(0,len(list_a)):
		if winner_found:
			break
		x = list_a[row][0]
		#print "x is "+str(x)
		if x==0:
			continue
		for col in range(1,len(list_a[x])):
			y = list_a[row][col]
			#print "y is "+str(y)
			if y!=x:
				break
			elif col==len(list_a[col])-1:
				print "Player "+str(x)+" is the winner!"
				winner_found = True
				break
				
	#next find vertical with identical entries (non-zero)
	if not winner_found:
		for col in range(0,len(list_a[0])):
			if winner_found:
				break
			x = list_a[0][col]
			#print "x is "+str(x)
			if x==0:
				continue
			for row in range(1,len(list_a)):
				y = list_a[row][col]
				#print "y is "+str(y)
				if y!=x:
					break
				elif row==len(list_a)-1:
					print "Player "+str(x)+" is the winner!"
					winner_found = True
					break
					
	#finally find a diagonal with identical entries (non-zero)
	#only have to search 2 diagonals, from top left and top right
	#step downward from top left
	if not winner_found:
		x = list_a[0][0]
		#print "x is "+str(x)
		if x!=0:
			for i in range(1,len(list_a)):
				y = list_a[i][i]
				#print "y is "+str(y)
				if y!=x:
					break
				elif i==len(list_a)-1:
					print "Player "+str(x)+" is the winner!"
					winner_found = True
					break
					
	#step downward from top right
	if not winner_found:
		x = list_a[0][len(list_a)-1]
		#print "x is "+str(x)
		if x!=0:
			for i in range(1,len(list_a)):
				y = list_a[i][len(list_a)-1-i]
				#print "y is "+str(y)
				if y!=x:
					break
				elif len(list_a)-1-i==0:
					print "Player "+str(x)+" is the winner!"
					winner_found = True
					break
					
	if not winner_found:
		print "Tie game!"
	return winner_found
		
def play_ttt(game_board):
	for i in range(0,len(game_board)):
		print game_board[i]
	while not who_won_ttt(game_board):
		valid_play = False
		zero_found = False
		while not valid_play:
			coords1 = raw_input("Player 1 enter coordinates to play on (in format row,col): ")
			row = int(coords1.split(",")[0])-1
			col = int(coords1.split(",")[1])-1
			if game_board[row][col]!=0:
				print "Those coordinates have already been played. Please try again."
			else:
				game_board[row][col] = 1
				valid_play = True
				for i in range(0,len(game_board)):
					print game_board[i]
					if 0 in game_board[i]:
						zero_found = True
		if who_won_ttt(game_board) or not zero_found:
			break
		valid_play = False
		while not valid_play:
			coords2 = raw_input("Player 2 enter coordinates to play on (in format row,col): ")
			row = int(coords2.split(",")[0])-1
			col = int(coords2.split(",")[1])-1
			if game_board[row][col]!=0:
				print "Those coordinates have already been played. Please try again."
			else:
				game_board[row][col] = 2
				valid_play = True
				for i in range(0,len(game_board)):
					print game_board[i]
					
def max_of_three(x,y,z):
	if x>y and x>z:
		return x
	elif y>x and y>z:
		return y
	elif z>x and z>y:
		return z
	else:
		return "2 or more of the 3 numbers are equal; no max found"

def pick_word(f):
	with open(f,"r") as open_file:
		word_list = []
		line = open_file.readline()
		while line:
			word_list.append(line)
			line = open_file.readline()
	return random.choice(word_list).strip()

	
def print_inc_word(incomplete_word):
	for i in range(0,len(incomplete_word)):
		print incomplete_word[i],
	print ""
def guess_letters(f):
	while True:
		print "Welcome to Hangman!"
		word = pick_word(f)
		incomplete_word = []
		
		for i in range(0,len(word)):
			incomplete_word.append("_")
		print_inc_word(incomplete_word)
		#print str(len(word))+" "+str(len(incomplete_word))
		
		word_complete = False
		penalty = 0
		already_guessed = []
		while not word_complete and penalty<6:
				
			guess = raw_input("Guess your letter: ")
		
			if guess in already_guessed:
				print "You've already guessed this letter! Try again."
				print_inc_word(incomplete_word)
				continue
			else:
				already_guessed.append(guess)
			
			if guess in word:
				for i in range(0,len(word)):
					if word[i]==guess:
						incomplete_word[i] = guess
				print_inc_word(incomplete_word)
				if "_" not in incomplete_word:
					word_complete = True
					new_game = raw_input("You win! Start new game? (Y/N) ")
					if new_game=="N":
						return
			else:
				print "Incorrect!"
				penalty+=1
				if penalty==5:
					print "Only "+str(int(6-penalty))+" incorrect guess left!"
				elif penalty<6:
					print "Only "+str(int(6-penalty))+" incorrect guesses left!"
				else:
					new_game = raw_input("You lose! Start new game? (Y/N) ")
					if new_game=="N":
						return
				print_inc_word(incomplete_word)
				
def birthday_dictionary():
	b_dict = {"Albert Einstein":"03/14/1879","Benjamin Franklin":"01/17/1706","Ada Lovelace":"12/10/1815"}
	print "Welcome to the birthday dictionary. We know the birthdays of:"
	for name in b_dict.keys():
		print name
	name = raw_input("Whose birthday do you want to look up?\n")
	print name+"'s birthday is "+b_dict[name]
	

def birthday_json(f):
	with open(f,"r") as open_file:
		b_dict = json.load(open_file)
		
	print "Welcome to the birthday dictionary. We know the birthdays of:"
	for name in b_dict.keys():
		print name
		
	name = raw_input("Whose birthday do you want to look up?\n")
	print name+"'s birthday is "+b_dict[name]
	
	req = raw_input("Would you like to add another scientist's name and birthday to the dictionary? (Y/N) ")
	if req=="Y":
		new_name = raw_input("Great! Please enter the name of the scientist: ")
		new_DOB = raw_input("Now enter their DOB (MM/DD/YYYY): ")
		b_dict[new_name] = new_DOB
		with open(f,"w") as open_file:
			json.dump(b_dict,open_file)
			
def birthday_months(f):
	with open(f,"r") as open_file:
		b_dict = json.load(open_file)
	
	birth_month_numbers = {"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}
	DOB_months = []
	print "Welcome to the birthday dictionary. We know the birthdays of:"
	for name in b_dict.keys():
		print name
		DOB = b_dict[name]
		DOB_month_num = DOB.split("/")[0]
		DOB_months.append(birth_month_numbers[DOB_month_num])
	
	print "Here are the birth months of scientists in the database and how many were born in each month:"
	c = Counter(DOB_months)
	print "{"
	for k,v in c.most_common():
		print "\t"+k+": "+str(v)
	print "}"
	return c

def bokeh_sample():
	output_file("plot.html")
	x = [10,20,30]
	y = [4,5,6]
	p = figure()
	p.vbar(x=x,top=y,width=0.5)
	show(p)
	
def birthday_plots(f):
	data = birthday_months(f)
	output_file("birthday_data.html")
	x = data.keys()
	x_categories = data.keys()
	y = data.values()
	p = figure(x_range=x_categories) #This is to get a non-numerical x-axis value to work in the plot
	p.vbar(x=x,top=y,width=0.5)
	show(p)
	
def main():
	#who_won_ttt([[1,0,1],
	#			 [2,2,2],
	#			 [1,0,1]])
	#play_ttt([[0,0,0],
	#		  [0,0,0],
	#		  [0,0,0]])
	#print max_of_three(7,6,4)
	#picked_word = pick_word("sowpods.txt")
	#print picked_word
	#print len(picked_word)
	#guess_letters("sowpods.txt")
	#birthday_dictionary()
	#birthday_json("birthday_dictionary.json")
	#birthday_months("birthday_dictionary.json")
	#bokeh_sample()
	birthday_plots("birthday_dictionary.json")
	
if __name__ == "__main__":
	main()
