import numpy as np

def grad(y,x,w):
	return ((w.dot(x.T) - y.T).dot(x))/x.shape[0]

gt = []
f = open('./uci.dat','r')
data = []
lines = f.readlines()
for l in lines:
	data += [l[:-1].split('\t')[:5]]
	gt += [l[:-1].split('\t')[-1]]

data = np.array(data, dtype=np.float32)
gt = np.array(gt, dtype=np.float32)
print(data)
print(gt)
data = (data - np.mean(data, axis = 0))/np.std(data, axis = 0)
n = 0.25

N = data.shape[0]
w = np.zeros(5).reshape(1,5)
gt = gt.reshape(gt.shape[0],1)
ep = 1e-6
loss = []
l = np.sum((gt - data.dot(w.T))**2)/N
loss += [l]
H = (data.T).dot(data)/N
iter_bgd = 0

while True:
	iter_bgd += 1
	w = w - n*grad(gt,data,w)
	l = np.sum((gt - data.dot(w.T))**2)/N
	if ( abs(l - loss[-1]) < ep ) :
		break
	loss += [l]

w = np.zeros(5).reshape(1,5)
n = 0.25
ep = 1e-6
iter_opt = 0
loss = []
l = np.sum((gt - data.dot(w.T))**2)/N
loss += [l]

while True:
	iter_opt += 1
	g = grad(gt,data,w)
	n = (np.linalg.norm(g)**2)/(g.dot(H).dot(g.T))	
	w = w - n*grad(gt,data,w)
	l = np.sum((gt - data.dot(w.T))**2)/N
	if (abs(l - loss[-1]) < ep ):
		break
	loss += [l]		

loss = []
iter_new = 0
w = np.zeros(5).reshape(1,5)
n = 0.25
ep = 1e-6
l = np.sum((gt - data.dot(w.T))**2)/N
loss += [l]
while True:
	iter_new += 1
	g = grad(gt,data,w)
	w = w - g.dot(np.linalg.inv(H))
	l = np.sum((gt - data.dot(w.T))**2)/N
	if (abs(l - loss[-1]) < ep ):
		break
	n = (np.linalg.norm(g)**2)/(g.dot(H).dot(g.T))	
	loss += [l]		


print("Batch gradient Decent: ",iter_bgd)
print("Optimal learning rate gradient Decent: ",iter_opt)
print("Newton's method gradient Decent: ",iter_new)