from kmeans import *

def test_distance(N):
	rng = 100
	for i in xrange(0,N):
		x1 = np.random.rand() * rng
		x2 = np.random.rand() * rng
		y1 = np.random.rand() * rng
		y2 = np.random.rand() * rng

		result = distance(np.array([x1,y1]),np.array([x2,y2]))
		valid  = np.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
		if result != valid:
			print 'ERROR!'
			print 'result: ',result
			print 'valid: ',valid

test_distance(1000)