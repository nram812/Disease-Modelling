import numpy as np

def generate_pts(n_pts):
    x = np.linspace(-100,100,n_pts)
    y = np.linspace(-100,100,n_pts)
    return np.meshgrid(x, y)
def dist_function(x_arr, y_arr, x_ref, y_ref):
    return ((x_arr - x_ref)**2 + (y_arr - y_ref)**2)**(1/2.0)

def iterate_pts(X, Y):
    distance = dist_function(X, Y, 0, 0)
    angle = np.arctan2(X, Y)
    cond = distance <= 200
    X_update = X.copy()
    Y_update = Y.copy()

    del_x = 0.5
    del_y = 0.5
    X_update[cond] = X[cond] + (np.random.normal(0,1,X[cond].shape)) * del_x
    Y_update[cond] = Y[cond] + (np.random.normal(0,1,Y[cond].shape)) * del_y

    X_update[~cond]= X[~cond] -np.sin(angle[~cond])  *del_x
    Y_update[~cond] = Y[~cond] - np.cos(angle[~cond]) * del_y
    return X_update, Y_update



iteration = 500
X_0, Y_0 = generate_pts(50)
X, Y = X_0,Y_0
x_infected = [25]
y_infected = [25]

for i in range(iteration):
    X, Y = iterate_pts(X, Y)
    for i in range(len(x_infected)):
        # this loop can be completed in parallel
        cond = np.where(dist_function(X, Y, X[x_infected[i],y_infected[i]],
                                      Y[x_infected[i],y_infected[i]]) < 0.5)

        # note this marks thenn as stationary
        x_infected += cond[0].tolist()
        y_infected += cond[1].tolist()



import pylab as py
py.figure()
py.plot(X.ravel(),Y.ravel(), 'rx')
py.plot(X_0.ravel(),Y_0.ravel(), 'kx')
py.plot(X[x_infected,y_infected],
        Y[x_infected,y_infected], 'yx')

