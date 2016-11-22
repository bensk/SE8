for x in range(10):
	if x % 2 == 1:
		print "%s is odd" % x
# What will print?

for x in range(1,10):
	if x % 3 == 0:
		print "I like these numbers"
# How many numbers will print?

for x in ("hello"):
	print x
# What will print?

vowels = ['a','e','i','o','u']
sentence = raw_input("Give me a sentence")
sntnc = []
for x in sentence:
	if x not in vowels:
		sntnc.append(x)
print "".join(sntnc)
