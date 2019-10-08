import numpy as np

new_w = np.array([1, 0, -1])[:,np.newaxis]

neta = 0.1
w = np.array([1, 0, 0])[:,np.newaxis]

from copy import deepcopy
t = np.array([-1, -1, 1, -1, 1, 1])[:,np.newaxis]

ind = np.where(t != 0)
X = np.array([[1, 1, 1], [-1, -1, 1], [2, 2, 1], [-2, -2, 1], [-1, 1, 1], [1, -1 ,1]])

while(len(ind[0])>0):
    w = deepcopy(new_w)
    y = X@w
    o = np.where(y > 0, 1, -1)
    z = t-o
    ind = np.where(z != 0)
    new_w = w + neta*(X[ind[0]].T@z[ind[0]])
    print("->>>>\n",ind[0],"\n",  new_w)
