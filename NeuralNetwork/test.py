import numpy as np
from ann import pre,feedfwd,backprop
from func import *

PASSED 	= 'passed'
RESULT 	= 'result'
RET    	= 'ret'
CORRECT = 'correct'

def test_pre():
	print "TEST PRE"
	x = np.array([2])
	w = np.array([1,2])
	b = np.array([2,4])
	print 1 * x + 2
	print 2 * x + 4
	print pre(x,w,b)

	x = logistic(np.array([2]) * np.array([1,2]) + np.array([2,4]))
	w = np.array([[2,1],[3,5]])
	b = np.array([2,1])
	print 2 * x[0] + 1 * x[1] + 2
	print 3 * x[0] + 5 * x[1] + 1
	print pre(x,w,b)

def init(rand_init=True):
	rand = lambda : int(np.random.rand() * 10)
	x = np.array([rand() if rand_init else 2 for i in xrange(0,2)])

	w111 = rand() if rand_init else 1
	w112 = rand() if rand_init else 2
	w121 = rand() if rand_init else 1
	w122 = rand() if rand_init else 2
	w211 = rand() if rand_init else 2
	w212 = rand() if rand_init else 3
	w221 = rand() if rand_init else 1
	w222 = rand() if rand_init else 5
	w311 = rand() if rand_init else 2
	w312 = rand() if rand_init else 3
	w321 = rand() if rand_init else 1
	w322 = rand() if rand_init else 4
	w    = [np.array([[w111,w121],[w112,w122]]), np.array([[w211,w221],[w212,w222]]), np.array([[w311,w312],[w321,w322]])]

	b11 = rand() if rand_init else 2
	b12 = rand() if rand_init else 4
	b21 = rand() if rand_init else 2
	b22 = rand() if rand_init else 1
	b31 = rand() if rand_init else 1
	b32 = rand() if rand_init else 2
	b   = [np.array([b11,b12]),np.array([b21,b22]),np.array([b31,b32])]

	return locals()

f = logistic

def test_feedfwd():
	globals().update(init())
	z11 = x[0] * w111 + x[1] * w121 + b11
	z12 = x[0] * w112 + x[1] * w122 + b12
	# print 'z1 (correct): ',z11,z12
	y11 = f(z11)
	y12 = f(z12) 

	# print 'y1 (correct): ',y11,y12
	z21 = y11 * w211 + y12 * w221 + b21
	z22 = y11 * w212 + y12 * w222 + b22
	# print 'z2 (correct): ',z21,z22
	y21 = f(z21)
	y22 = f(z22)

	# print 'y2 (correct): ',y21,y22
	y31 = y21 * w311 + y22 * w321 + b31
	y32 = y21 * w312 + y22 * w322 + b32

	out = linear(np.array([y31,y32]))

	delta = 0.1
	# print 'valid:  \t',out
	# v = feedfwd(x,w,b,f,softmax)['output']
	v = feedfwd(x,w,b,f,linear)['output']
	# print 'feedfwd:\t',v
	t = np.abs(out - v) < delta
	return {PASSED : t.all(), RESULT : {RET : v, CORRECT : (out,np.abs(out - v))}}

def test_backprop():
	globals().update(init(rand_init=False))
	step = 1
	target = 2

	res = feedfwd(x, w, b, f, softmax)
	# print res
	error_out = dsqrerr(res['output'], target)
	
	print res
	return { PASSED : False, RESULT : 'Not Implemented' }

def test(t,n):
	for i in xrange(0,n):
		res = t()
		if not res[PASSED]:
			print 'Error -> Returned: %s, Correct: %s' % (res[RESULT][RET],res[RESULT][CORRECT])
			return

# test_pre()
print "TEST FEEDFWD"
test(test_feedfwd, 1000)
# print "TEST BACKPROP"
# test(test_backprop, 1)