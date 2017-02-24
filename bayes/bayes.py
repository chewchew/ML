
characters = [
	 'MERCUTIO'
	,'ROMEO'
	,'PETER'
	,'SAMPSON'
	,'TYBALT'
	,'FRIAR JOHN'
	,'FRIAR LAURENCE'
	,'LADY CAPULET'
	,'JULIET'
	,'PRINCE'
	,'MONTAGUE'
	,'PARIS'
	,'BALTHASAR'
	,'NURSE'
	,'PAGE'
	,'GREGORY'
	,'ABRAHAM'
	,'LADY MONTAGUE'
	,'BENVOLIO'
	,'CAPULET'
]
lines = {}

def new_character(line):
	if line in characters:
		return line
	else:
		return None

with open('script.txt','r') as script:
	current = None
	dialogue = False

	for line in script:
		line = line.strip()

		if line.isupper():
			name = new_character(line)
			if name is not None:
				current = name
				if name not in lines:
					lines[name] = [[]]
					current = name
		else:
			# Dialogue begins/ends
			if len(line) == 0 and current is not None:
				dialogue = not dialogue
			# Dialogue underway
			if dialogue:
				if line != '':
					lines[current][-1].append(line)
			# Dialogue end
			else:
				if current is not None:
					lines[current].append([])
				current = None

for character,ls in lines.items():
	lines[character] = filter(lambda line : len(line) > 0, ls)
