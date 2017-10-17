import requests, random
from bs4 import BeautifulSoup

#The following function retrieves the html from a url
#using the requests library, and then using the 
#BeautifulSoup library extracts the article titles
#from a given news website, then prints them all
def get_page(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text,"html.parser")
	titles = soup.find_all(class_="story-heading")
	for t in titles:
		print (t.text.strip())
		
def get_all_text(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text,"html.parser")
	print (soup.find(class_="hed").getText())
	print (soup.find(class_="dek").getText())
	article_text = soup.find_all('p')
	for line in article_text:
		print (line.getText())
		
def write_to_file(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text,"html.parser")
	file_name = raw_input("Choose file name for output file: ")
	#The following code is how to create a file stream in Python,
	#then specify whether it's read or write
	with open(file_name,"w") as open_file:
		open_file.write(soup.find(class_="hed").getText())
		open_file.write(soup.find(class_="dek").getText())
		full_text = soup.find_all('p')
		for line in full_text:
			open_file.write(line.getText().encode("utf-8"))
		open_file.close()

def cows_and_bulls():
	numbers = "1234567890"
	random4dig = "".join(random.sample(numbers,4))
	print ("Welcome to the Cows and Bulls Game!")
	guesses = 0
	while True:
		cows = 0
		bulls = 0
		user_guess = raw_input("Enter a number: ")
		for i in range(0, 4):
			if user_guess[i] == random4dig[i]:
				cows += 1
			elif user_guess[i] in random4dig:
				bulls += 1
		cowPl = "cows"
		bullPl = "bulls"
		if cows == 1:
			cowPl = "cow"
		if bulls == 1:
			bullPl = "bull"
		print (str(cows)+" "+cowPl+", "+str(bulls)+" "+bullPl)
		guesses += 1
		if cows == 4:
			print ("That's correct! That took "+str(guesses)+" guesses!")
			break
		

def main():
	#get_page("https://www.nytimes.com/")
	#cows_and_bulls()
	#get_all_text("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
	write_to_file("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")

if __name__ == "__main__":
	main()
