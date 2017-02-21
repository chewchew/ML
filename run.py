import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from ann import run,feedfwd
from func import logistic

# Setup
n_inputs = 2
n_hid   = 1
n_units = 4
step    = 0.2
epochs  = 10
samples = 5000

# f   = lambda x : x ** 2
f = lambda x : np.linalg.norm(x)
rng = (-1,1)

# Run

# 3D
samples = 1.0*np.abs(rng[0] - rng[1])/math.sqrt(float(samples))
X, Y = np.mgrid[rng[0]:rng[1]:samples, rng[0]:rng[1]:samples]
xs = np.array(map(lambda e: np.array(list(e)),zip(X.ravel(), Y.ravel())))
print len(xs)
# 2D
# x = np.linspace(rng[0],rng[1],samples)
# xs = map(lambda e : np.array([e]), x)

data = [(x,f(x)) for x in xs]
(w,b),costs = run(data, n_inputs, n_hid, n_units, step, epochs)

# Plot 2D
# plt.plot(xs,[f(x) for x in xs])
# ys = map(lambda e: e['output'],[feedfwd(x, w, b, logistic) for x in xs])
# plt.plot(xs,ys)
# plt.show()

# Plot 3D
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
xs_plot = xs[:,0]
ys_plot = xs[:,1]
ys = map(lambda e: e['output'],[feedfwd(x, w, b, logistic) for x in xs])
plot_ann = ax1.scatter(xs_plot,ys_plot,ys)
plot_f   = ax1.scatter(xs_plot,ys_plot,[f(x) for x in xs])
plt.show()