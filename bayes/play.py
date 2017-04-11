import re
NEWLINE = 'newline'
HEADING = 'heading'
CHARACTER = 'character'
ACT = 'act'
SCENE = 'scene'
ENTER = 'enter'
LINE = 'line'

def parse(lines):
	for line in lines.split('\n'):
		if line == '':
			yield NEWLINE,line
		elif line.startswith('ACT'):
			yield ACT,line
		elif line.startswith('SCENE') or line.startswith('PROLOGUE'):
			yield SCENE,line
		elif line.startswith('\t') or line.startswith('    '):
			if line.find('Enter') != -1:
				yield ENTER,line
			else:
				yield LINE,line
		else:
			yield CHARACTER,line

character = lambda (label,line): label == CHARACTER

subtext = re.sub(r'\[(.*?)\]','',"[asd asd] asd")
def getWords(text):
    return re.compile('\w+').findall(text)

def strip(line):
	# line = re.sub(r'\[(.*?)\]','',line)
	return getWords(line.strip())

def get_lines(script_file,out_file):
	with open(script_file,'r') as script:
		text = script.read()
		lines = {}
		character_active = None
		nl_count = 0
		spoken = False
		for (label,line) in parse(text):
			if label == CHARACTER:
				character_active = line
				nl_count = 0
				if character_active not in lines:
					lines[character_active] = []
			elif label == NEWLINE:
				nl_count += 1
				spoken = False
			elif character_active and ((nl_count == 1 and label == LINE) or spoken):
				lines[character_active].append(strip(line))
			elif label == LINE:
				spoken = True

		with open(out_file,'w') as out:
			out.write(str(lines))

		# n_lines = map(lambda char: (char,len(lines[char])), lines.keys())
		# n_lines = filter(lambda (char,n): n > 100, n_lines)
		# print n_lines
		return {k:v for k,v in lines.iteritems() if len(v) > 100}

#get_lines('script.txt','out.txt')