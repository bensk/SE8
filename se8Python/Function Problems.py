"""
Functions to Define
"""

# check to see if a number is even or odd
def even_odd(number):

# Compare two numbers. Say which number is bigger, or if they're equal
def compare(number, number1):

#Insult generator. If user enters any name BUT yours, tell them what you really think. If they enter your name, compliment them
def insult(name):

is_even(42)
is_odd(13)
even_odd(32495078)
compare(26,13)
know_nothing("SK")

def even_odd(number):
	if number % 2 == 0:
		print "Even"
	else:
		print "Odd"

def compare(number, number1):
	if number > number1:
		print "%s is bigger than %s" % (number, number1)
	elif number < number1:
		print "%s is bigger than %s" % (number1, number)
	else:
		print "%s is %s" % (number, number1)

def know_nothing(name):
	if name == "Ben":
		print "You are awesome!"
	else:
		print "You know nothing!"

even_odd(32495078)
compare(26,13)
know_nothing("SK")
