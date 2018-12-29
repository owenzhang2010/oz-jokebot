import time
import csv
import sys
import os.path
import requests
import json

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

"""
gets JSON array of r/dadjokes posts and returns it (if successful)
"""
def reddit_req(url):
	r = requests.get(url, headers = {'User-agent': 'oz-jokebot'})
	if r.status_code != 200:
		print("An error happened with code " + str(r.status_code) + ". Joke's on you!")
		quit()
	return r.json()["data"]["children"]

"""
filter func, throws away jokes that are NSFW or that don't start with why, what or how
"""
def keep(post):
	first_word = post["data"]["title"].split(" ")[0].lower()
	starts_wwh = first_word == "why" or first_word == "what" or first_word == "how"
	return not post["data"]["over_18"] and starts_wwh

"""
converts to [prompt, punchline]
"""
def to_2list(post):
	return [post["data"]["title"], post["data"]["selftext"]]

if __name__ == "__main__":
	num_args = len(sys.argv)
	jokes = []
	if num_args == 1:
		data = list(filter(keep, reddit_req("https://www.reddit.com/r/dadjokes.json")))
		jokes = list(map(to_2list, data))
	elif num_args > 2:
		print("Too many arguments")
		quit()
	else:
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
