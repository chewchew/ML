
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

def new_character(line):
	if line in characters:
		return line
	else:
		return None

def get_lines(script):
	lines = {}

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
						lines[current][-1] += line.translate(None,'!?;:,').lower().split(' ')
				# Dialogue end
				else:
					if current is not None:
						lines[current].append([])
					current = None

	for character,ls in lines.items():
		lines[character] = filter(lambda line : len(line) > 0, ls)

	return lines

def word_count(script,excluded):
	lines = get_lines('script.txt')
	word_count = {}
	words = []

	for character,ls in lines.items():
		word_count[character] = {}
		for line in ls:
			for word in line:
				if word not in excluded:
					if word in word_count[character]:
						word_count[character][word] += 1
					else:
						word_count[character][word] =  1

					if word not in words:
						words.append(word)

	with open('out.txt','w') as f:
		f.write(str(word_count))
	return word_count,words

wcs,words = word_count('script.txt',['the'])
print len(words)
for character,word_count in wcs.items():
	print character, ': ', sorted(word_count.items(),key=lambda (k,v) : v)[-10:]

