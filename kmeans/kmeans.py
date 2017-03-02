import numpy as np
import random as r
import matplotlib.pyplot as plt
from copy import deepcopy

distance = lambda x,y: np.linalg.norm(x-y)

rnd = lambda rng,shift: np.random.rand() * rng - rng/2 - shift

tolist = lambda x : np.array(list(x))

def initialize(data,k):
	return np.array([np.array(list(deepcopy(x))) for x in r.sample(data,k)])

def unsetc(classes,point):
	classes[tuple(point)] = None

def setc(classes,i,point):
	classes[tuple(point)] = i

def order(classes):
	cs = {}
	for x,c in classes.items():
		if c not in cs:
			cs[c] = [tolist(x)]
		else:
			cs[c].append(tolist(x))
	return cs

def update_data(data,means,classes):
	for x in data:
		best   = np.inf
		best_i = 0
		for i,mean in enumerate(means):
			d = distance(x,mean)
			if d < best:
				best   = d
				best_i = i
		unsetc(classes,x)
		setc(classes,best_i,x)

def update_means(means,classes):
	cs = order(classes)
	for c,xs in cs.items():
		means[c] = np.sum(xs) / len(xs)

def kmeans(data,k):
	means = prev = initialize(data,k)
	classes = {tuple(x):None for x in data}
	for i in xrange(0,1000):
		update_data(data,means,classes)
		update_means(means,classes)
	update_data(data,means,classes)
	return classes,means

N = 10
rng = 10
shift1 = 20
shift2 = -20
data = np.array([np.array([rnd(rng,0 if i < N/3 else shift1 if i < 2*N/3 else shift2),rnd(rng,0 if i < N/3 else shift1 if i < 2*N/3 else shift2)]) for i in xrange(0,N)])
k = 2
classes,means = kmeans(data,k)

colors = ['b','r','c','m','y','k','w']

for c,xs in order(classes).items():
	print c,len(xs)
for c,xs in order(classes).items():
	for x in xs:
		plt.scatter(x[0],x[1],c=colors[c])
plt.scatter(means[:,0],means[:,1],c='g')
plt.show()