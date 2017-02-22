import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from ann import run,feedfwd
from func import logistic

# Setup
n_inputs = 1
n_outputs = 1
n_hid   = 3
n_units = 10
step    = 0.5
epochs  = 500
samples = 5000

f   = lambda x : np.sin(x) * (1 + np.sin(x))
# f = lambda x : np.linalg.norm(x)
rng = (0,2*np.pi)

# Run
def xs3D(rng,n):
	X, Y = np.mgrid[rng[0]:rng[1]:n, rng[0]:rng[1]:n]
	return np.array(map(lambda e: np.array(list(e)),zip(X.ravel(), Y.ravel())))

def xs2D(rng,n):
	x = np.linspace(rng[0],rng[1],samples)
	return map(lambda e : np.array([e]), x)

# 3D
# samples = 1.0*np.abs(rng[0] - rng[1])/math.sqrt(float(samples))
# xs = xs3D(rng,samples)

# 2D
xs = xs2D(rng,samples)

data = [(x,f(x)) for x in xs]
(w,b),costs = run(data, n_inputs, n_hid, n_units, n_outputs, step, epochs)


# Plot 2D
plt.figure()

plt.plot(xs,[f(x) for x in xs],'g--')
ys = np.array(map(lambda e: e['output'], [feedfwd(x, w, b, logistic, lambda zs : zs) for x in xs]))
plt.plot(xs,ys,'r')

plt.figure()
plt.plot(range(0,len(costs)),costs)

# Plot 3D
# fig = plt.figure()
# ax1 = fig.add_subplot(111, projection='3d')
# xs_plot = xs[:,0]
# ys_plot = xs[:,1]
# ys = map(lambda e: e['output'],[feedfwd(x, w, b, logistic, lambda zs : zs) for x in xs])
# plot_ann = ax1.scatter(xs_plot,ys_plot,ys)
# plot_f   = ax1.scatter(xs_plot,ys_plot,[f(x) for x in xs])

plt.show()