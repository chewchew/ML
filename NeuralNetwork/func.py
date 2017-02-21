import numpy as np
import math

def logistic(z):
	return 1 / (1 + np.exp(-z))

def dlogistic(z):
	f = logistic(z)
	return f * (1 - f)

def sqrerr(y,t):
	return ((t - y) * (t - y))/2

def dsqrerr(y,t):
	return y - t

def softmax(ys):
	e_ys = sum(np.exp(ys))
	return np.array([np.exp(y) / e_ys for y in ys])

def linear(zs):
	return zs