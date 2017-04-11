import re

character = re.compile(r'[A-Z]*\n\n(\t((?P<enter>Enter [A-Z]*)|(?P<line>[\w ]+))\n)*',re.M)
with open('test.txt','r') as f:
	text = f.read()
	m = character.search("JOHAN\n\n\tasdasd\n\tBeats down their swords\n\tEnter TYBALT\n\tEnter JOHAN\n")
	if m:
		print m.group('enter').split()
	else:
		print 'No match!'