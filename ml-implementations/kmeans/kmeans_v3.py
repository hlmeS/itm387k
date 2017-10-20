#! /usr/bin/env python2

"""
ICS635 - K-Means

Author: Holm Smidt
Date: 2016-10-01

Overview:
This is an implementation of a K-Means algorithm using
the euclidean squared distance measure as the distortion
fu0nction.
Data was generated using multiple Gaussian distribution
with defined means and covariances.
The implementation explores the role of various parameters.

"""
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse


def importData(s):
    """ this is a general template for
        importing data from a text file  """
    data = np.genfromtxt(s, delimiter=',')
    dim = len(data[1,:])
    X = data[:, [0, dim-2]]
    L = data[:, [dim-1]]
    return X, L

def generateGaussian(m, mean, cov):
    """ generate multivariate Gaussian
        with m examples, means in mean,
        and covariance matrix cov.     """
    return np.random.multivariate_normal(mean, cov, m)

def cost(data, centroids, assignment):
    """ calculate total cost over all data points """
    m = len(data[:,1])
    n = len(data[1,:])
    K = len(centroids[:,1])
    dist = np.zeros((K,1))

    for k in range(0,K):
        X = data[np.nonzero(assignment[:,k]),:]
        X = X.reshape(len(X[0,:]), n)
        for i in range(0, len(X)):
            dist[k] += distortion(X[i,:], centroids[k,:])

    return dist


def distortion(u,v):
    """ squared euclidean distance """
    return np.dot(np.subtract(u,v),np.subtract(u,v))


def assignColors(A, colors):
    """ assign colors based on classification """

    col = np.chararray((len(A[:,0])))
    for i in range(0, len(col)):
        col[i] = colors[np.argmax(A[i,:])]

    return col

""" adapted from stackoverflow: """
def plot_cov_ellipse(cov, mu, nstd=2, ax=None, **kwargs):

    def eigsorted(cov):
        vals, vecs = np.linalg.eigh(cov)
        order = vals.argsort()[::-1]
        return vals[order], vecs[:, order]

    if ax is None:
        ax = plt.gca()


    #for cov, mean in zip(sigma, mu):
    vals, vecs = eigsorted(cov)
    theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))
    width, height= 2 * nstd * np.sqrt(vals)
    ellip = Ellipse(xy=mu, width=width, height=height, angle=theta, **kwargs)

    ax.add_artist(ellip)

    return ellip


def KMeans(data, clusters, iters, J_theory, sigma, mu, Ks, test, **kwargs):
    """ K-Means algorithm

        *givens: data (matrix), number clusers (int)
        *rand_inits (int): # random cluster assignments

    """

    """ shuffle data well   """
    #for i in range(0, 10*len(data)):
    #    np.random.shuffle(data)

    PRINT = True
    X = data
    m = len(X[:,1])
    n = len(X[1,:])
    K = clusters
    A = np.zeros((m,K), dtype=np.int)
    J_r = np.zeros((iters))          # cost for each random iteration
    J_i = [100, 0]                        # cost for each kMean iteration
    epsilon = 0.1                         # marginal difference when to stop

    """ loop iters times   """
    iter = 0
    while (iter < iters):
        iter += 1

        if 'initC' in kwargs:
            C = kwargs['initC']
        else:
            C = np.concatenate((random.sample(X, K))).reshape(K, n) # centroids randomly chosen from data set

        if PRINT: print "initial means ",  C
        C_col = np.zeros((K,n))

        # just for plotting, reset here as well
        A = np.zeros((m,K), dtype=np.int)


        J_i = [0.0, 100.0]          # first value will remain dummy value, then we start appending to the list
        iteration = 0

        """ run K-Means until we don't see much improvement anymore """
        while (abs((J_i[1] - J_i[0]) if iteration == 0 else (J_i[iteration]-J_i[iteration -1])) > epsilon):


            """ plot if data is 2D and less than 8 clusters """
            plotEachIteration = True
            if plotEachIteration:
                if n == 2 and K < 8:
                    colors = ['b', 'r', 'g', 'c', 'k', 'm', 'y']
                    dataColors = assignColors(A, colors)
                    fillColors = colors[0:K]

                    fig = plt.figure()
                    fig.clf()
                    ax = fig.add_subplot(111)
                    ax.grid(True, linestyle='-', color='0.75')
                    ax.set_xlim([X[:, 0].min() -2, X[:,0].max()+2])
                    ax.set_ylim([X[:, 1].min() -2, X[:,1].max()+2])

                    title = 'K Means Learning, k='+'%02d' %(K)+', m='+'%03d' %(m)+', iter='+'%02d' %(iteration)
                    ax.set_title(title)
                    ax.set_xlabel("x1")
                    ax.set_ylabel("x2")

                    filename = 'results/training5K/'+'%02d' %(iter)+'/'  +'%04d' % (iteration)+'.png'

                    #fillColors = ['green', 'red', 'blue']
                    for cov, mean, col in zip(sigma, mu, fillColors):
                        plot_cov_ellipse(cov, mean, nstd=3, alpha=.2, color=col)

                    for x,y,z in zip(X[:,0], X[:,1], dataColors):
                        plt.scatter(x, y, c=z)
                    plt.scatter(C[:,0], C[:, 1], marker="o",s=70, c='c')

                    plt.savefig(filename, bbox_inches='tight')
                    #fig.close()
                    #plt.show()

            iteration += 1;

            """ K-Means First Step: Assign to centroids """
            dist = np.zeros((K, 1))
            A = np.zeros((m, K), dtype=np.int)      # reset assignment matrix to 0 for each iteration

            for i in range(0, m):                   # loop over training examples
                for k in range(0, K):               # compute for each cluster
                    dist[k] = distortion(X[i,:], C[k, :])   #use squared distance distortion, s.a.
                A[i, np.argmin(dist)] = 1           # choose smallest one and assign 1 to cluster

            """ K-Means Second Step: Move centroid """
            if not test:
                s = np.zeros((K, 1), dtype=float)       # need no. of samples assigned to each cluster
                for i in range(0, K):
                    s[i] = 1.0/(np.sum(A[:,i] , dtype=float))   #sum each column (inverse for averaging in next step)

                C = s * np.dot(np.transpose(A), X)      # new centroids result from matrix multiplication of A and X

            if iteration == 1:
                J_i[1] = np.sum(cost(X, C, A))
                C_col = C
            else:
                J_i.append(np.sum(cost(X,C,A)))
                C_col = np.vstack((C_col, C))
                #print "shape of C_col: ", np.shape(C_col)
                #print "shape of C: ", np.shape(C)

                if PRINT:
                    print "new centroids: ", C
                    print "Iteration: ", iteration
                    print "cost: ", J_i[iteration]
                    print "delta: ", (J_i[iteration] - J_i[iteration -1])

            if test: J_i[0]= J_i[1]


        J_r[iter-1] = J_i[-1]  # just keep the last value
        plotCostPerIteration = False
        if plotCostPerIteration:
            fig = plt.figure()
            fig.clf()
            i = np.arange(1, iteration+1, 1)
            plt.plot(i, abs(J_i[1:]/J_theory), 'b--')
            t = np.ones(np.shape(i))
            plt.plot(i, t, 'r--')
            plt.show()

    plotCostPerRandInit = True
    if plotCostPerRandInit and not test:
        i = np.arange(1, iter+1, 1)
        t = np.ones(np.shape(i))
        title = 'K Means Clustering, k='+'%02d' %(K)+', m='+'%03d' %(m)

        init_plot(title, [1, i.max()+0.5], [0,10],
                "Cluster Initialization Iteration",
                "Relative Distortion")

        plt.plot(i, abs(J_r/J_theory), 'b--', label="K-Means")
        plt.plot(i, t, 'r--', label="Known")
        plt.legend(loc=1)
        plt.savefig('results/trainingTest/CostPerRandInit_20p'+'%03d' %(Ks)+'.png', bbox_inches='tight')
        #plt.show()

    """ return performance and final cluster centroids"""
    if not test:
        print np.argmin(J_r)
        return (J_r, C_col[np.argmin(J_r):np.argmin(J_r)+K])
    else: return J_r

def init_plot(title, xlim, ylim, xlabel, ylabel):
    fig = plt.figure()
    fig.clf()
    ax = fig.add_subplot(111)
    ax.grid(True, linestyle = '-', color = '0.75')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)


def rotate2D(mat, degrees):
    x = math.radians(degrees)

    rot =  np.array([[math.cos(x), -math.sin(x)],
                     [math.sin(x), math.cos(x)]])

    return np.dot(mat, rot)

if __name__ == "__main__":

    ''' generate data '''
    n = np.array([20, 20])
    centroids = np.array([  [1,2],
                            [4,9]])
    cov = np.array([ [[.7, 0],[0 , 1.3]],
                     [[.4, 0],[0 , .1]] ])

    #rotate eclipses if desired
    #for i,x in zip([0,1,2,3], [0, 25, 0]):
    #    cov[i] = rotate2D(cov[i], x)

    edata = generateGaussian(n[0], centroids[0], cov[0])
    for i in range(1, len(n)):
        edata = np.concatenate((edata, generateGaussian(n[i], centroids[i], cov[i] )), axis=0)

    mask = np.random.choice([False,True], len(edata), p=[0.2, 0.8])

    trainData = edata[mask]
    testData = edata[np.logical_not(mask)]

    """ compute theoretical cost """
    nd = np.zeros((np.shape(n)), dtype=np.int)
    for i in range(0,len(nd)):
        nd[i] = n[i]
        if (i>0):
            nd[i] += nd[i-1]
    assign = np.zeros((len(edata[:,0]), len(centroids[:,0])), dtype=np.int)
    assign[0:n[0], 0] = 1
    for i in range(1, len(n)):
        assign[nd[i-1]:(nd[i]), i] = 1

    trainA = assign[mask]
    testA = assign[np.logical_not(mask)]


    #for data, assignment in zip((trainData, testData), (trainA, testA)):

    J_theory_train = cost(trainData, centroids, trainA)
    J_theory_test = cost(testData, centroids, testA)

    #print J_theory

    """ single loop with known K """
    '''
    # KMeans(data, clusters, rand_inits, theoretical_value):
    test = True
    J_train, C = KMeans(trainData, 5, 10, np.sum(J_theory_train), cov, centroids, 5, False)
    J_test = KMeans(testData, 5, 1, np.sum(J_theory_test), cov, centroids, 5, True, initC = C)
    print "J_theory Train: ", np.sum(J_theory_train)
    print "J_actual Train: ", np.min(J_train)
    print "J_theory Test: ", np.sum(J_theory_test)
    print "J_actual Test: ", np.min(J_test)
    '''

    """ loop over different no. of K's """

    #Ks = np.arange(2, int(0.8*len(data)), 1, dtype=np.int)
    Ks = np.arange(2,8,1,dtype=np.int)
    J_train_ks = np.zeros(len(Ks))
    J_test_ks = np.zeros(len(Ks))

    for j in range(len(Ks)):
        J_temp, C = KMeans(trainData, Ks[j], 25, np.sum(J_theory_train), cov, centroids, Ks[j], False)
        J_train_ks[j] = np.amin(J_temp)
        print " shape of C: ", np.shape(C)
        #J_test_ks[j] = np.amin(KMeans(testData, Ks[j], 1, np.sum(J_theory_test), cov, centroids, Ks[j], True, initC = C))

    """ plot """
    """
    i = np.arange(2, (len(Ks)+2), 1, dtype=np.int)
    t = np.ones(np.shape(i))
    title = 'K Means Clustering, K='+'%02d' %(Ks[0])+'-'+'%03d' %(Ks[-1])+', mtrain='+'%03d' %(len(trainData))+', mtest='+'%03d' %(len(testData))
    init_plot(title, [2, i.max()+0.5], [0,10], "K", "Relative Distortion")
    plt.plot(i, (J_train_ks/np.sum(J_theory_train)), 'b--', label="Training")
    plt.plot(i, (J_test_ks/np.sum(J_theory_test)), 'g--', label="Testing")
    plt.plot(i, t, 'r--', label="Known")
    plt.legend(loc=1)
    plt.savefig('results/trainingTest/CostPerK_20p.png', bbox_inches='tight')
    """
