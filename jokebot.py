import time

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

print(encore())