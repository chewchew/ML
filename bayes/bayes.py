from __future__ import division
import play
import pickle
import math

def mean(features,labels):
	pass

def flatten(xs): return reduce(lambda x,y: x + y, xs)

def extract_vocab(words):
	vocab = {}
	for word in words:
		if word not in vocab:
			vocab[word] = 1
	return vocab.keys()

def train(lines):
	vocab = extract_vocab( flatten(flatten(lines.values())) )
	prior = { character : 0 for character in lines.keys() }
	cond_prob = { word : { character : 0 for character in lines.keys() } for word in vocab }
	total_lines = len(flatten(lines.values()))
	count_word = {word : 0 for word in vocab}
	for character,lines in lines.items():
		c_lines = len(lines)
		prior[character] = c_lines/total_lines
		text = flatten(lines)
		for word in vocab:
			count_word[word] = len(filter(lambda x : x == word,text))
		for word in vocab:
			cond_prob[word][character] = (count_word[word] + 1) / (sum(count_word.values()) + 1)
	return vocab,prior,cond_prob

def naive_bayes(classes,vocab,prior,cond_prob,feature):
	vocab_f = extract_vocab( filter(lambda x : x in vocab,feature) )
	score = {}
	for c in classes:
		# score[c] = prior[c]
		score[c] = math.log(prior[c])
		for word in vocab_f:
			# score[c] *= cond_prob[word][c]
			score[c] += math.log(cond_prob[word][c])
	return score

if __name__ == '__main__':
	lines = play.get_lines('script.txt','out.txt')
	print lines.keys()

	# TRAINING
	# vocab,prior,cond_prob = train(lines)
	# pickle.dump(vocab,open('vocab','wb'))
	# pickle.dump(prior,open('prior','wb'))
	# pickle.dump(cond_prob,open('cond_prob','wb'))

	# APPLICATION
	vocab = pickle.load(open('vocab','rb'))
	prior = pickle.load(open('prior','rb'))
	cond_prob = pickle.load(open('cond_prob','rb'))
	res = naive_bayes(lines.keys(),vocab,prior,cond_prob,[])
	for k,v in sorted(res.items(),key=lambda (k,v) : v):
		print k,v