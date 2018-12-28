import time
import csv
import sys
import os.path

"""
Tells one joke, given a prompt and punchline
returns nothing
"""
def tell_joke(prompt, punchline):
	print(prompt)
	time.sleep(2)
	print(punchline)

"""
Determine whether to continue telling jokes
returns a boolean
"""
def encore():
	x = input("Type 'next' if you're awesome, 'quit' if you're a square: ")
	while x != "next" and x != "quit":
		x = input("I don't understand. Type 'next' if you're awesome, 'quit' if you're a square: ")
	if x == "next":
		return True
	else:
		return False


"""
Reads jokes from a csv, determines if it's valid joke format or not
returns a validation bool and a list of lists (prompt, punchline)
"""
def read_csv(file):
	joke_list = []
	valid = True
	with open(file, newline='') as f:
		reader = csv.reader(f)
		for row in reader:
			joke_list.append(row)
			if len(row) != 2: # not (prompt, punchline)
				valid = False
	return valid, joke_list

if __name__ == "__main__":
	num_args = len(sys.argv)
	if num_args == 1:
		print("No joke file given")
		quit()
	elif num_args > 2:
		print("Too many arguments")
		quit()
	if not os.path.isfile(sys.argv[1]):
		print("File doesn't exist")
		quit()
	name, ext = os.path.splitext(sys.argv[1])
	if ext != '.csv':
		print("File provided is not a csv")
		quit()
	valid, jokes = read_csv(sys.argv[1])
	if not valid:
		print("File is not a valid joke file")
		quit()
	for joke in jokes: 				# joke is a 2-item list
		tell_joke(joke[0], joke[1])
		if not encore():
			break
