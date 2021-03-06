import numpy as np
from func import *
from copy import deepcopy

pre_ = lambda v : sum(v) if isinstance(v,np.ndarray) else v
def pre(x,w,b):
	xw = w * x
	if isinstance(xw[0],np.ndarray):
		return np.sum(xw,axis=1) + b
	else:
		return xw + b

def feedfwd(x,w,b,f,out_f):
	inputs  = []
	ys = x
	for w_l,b_l in zip(w,b)[:-1]:
		zs = pre(ys,w_l,b_l)
		inputs.append((ys,zs))
		ys = f(zs)
	zs = sum(w[-1] * ys.reshape(len(ys),1)) + b[-1]
	inputs.append((ys,zs))
	output = out_f(zs)
	return { 'inputs' : inputs, 'output' : output }

def backprop(inputs,error,ws,bs,df,step):
	layers = reversed(list(enumerate(inputs[:-1])))
	
	x_l,z_l = inputs[-1]
	dfy = error * df(z_l)
	dw =  x_l.reshape(len(x_l),1) * dfy.reshape(1,len(dfy))
	db = dfy
	error =  np.sum(ws[-1] * dfy)
	
	ws[-1] = ws[-1] - step * dw
	bs[-1] = bs[-1] - step * db

	for i,(x_l,z_l) in layers:
		dfy = error * df(z_l)
		dw = dfy.reshape(len(dfy),1) * x_l.reshape(1,len(x_l))
		db = dfy
		error = np.sum(ws[i] * dfy.reshape(len(dfy),1))
		
		ws[i] = ws[i] - step * dw
		bs[i] = bs[i] - step * db

init = lambda n_units : np.array([np.random.rand() for i in xrange(0,n_units)])

def weights(n_inputs,n_hid,n_units,n_outputs):
	ws = [[init(n_units) for j in xrange(0,n_units)] for i in xrange(0,n_hid-1)]
	ws.insert(0, [init(n_inputs) for j in xrange(0,n_units)])
	ws.append([init(n_outputs) for j in xrange(0,n_units)])
	return ws

def biases(n_hid,n_units):
	bs = [init(n_units) for i in xrange(0,n_hid)]
	bs.append(np.array([np.random.rand()]))
	return bs

f     = logistic
df 	  = dlogistic
f_out = lambda zs : zs

def validation(data,w,b):
	avg_error = 0
	for (x,t) in data:
		res = feedfwd(x, w, b, f, f_out)
		avg_error += sqrerr(res['output'], t)
	return avg_error / len(data)

def run(data,n_inputs,n_hid,n_units,n_outputs,step,epochs):
	w = weights(n_inputs,n_hid,n_units,n_outputs)
	b = biases(n_hid,n_units)
	ret = (w,b)
	n = len(data)

	costs = []
	best_cost = validation(data,w,b)
	best_epoch = 0
	for j in xrange(0,epochs):
		np.random.shuffle(data)
		validation_set = data[:n/5]
		for i,(x,t) in enumerate(data[n/5 : ]):
			res = feedfwd(x, w, b, f, f_out)
			derror = dsqrerr(res['output'], t)
			backprop(res['inputs'], derror, w, b, df, step)
		cost = validation(validation_set,w,b)
		costs.append(cost)
		if cost.all() < best_cost.all():
			ret = (deepcopy(w),deepcopy(b))
			best_cost = cost
			best_epoch = j
	print 'Best Cost (%s): ' % best_epoch,best_cost
	return ret,costs