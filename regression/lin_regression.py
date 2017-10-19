#! /usr/bin/env python2

"""

Title: Linear Regression Demo
Author: Holm Smidt
Version: 0.9
Date: 10-17-2017

Overview:
Linear regression for gradient descent method. Modeled after class notes from Andrew Ng's
Machine Learning Coursera class.


"""

""" Some imports """
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def readData(filename):
    """
    This is a general template for using numpy
    to turn data file into matrix (2D-array).

    Then we split data into predictor & response
    variables and return them.
    """
    data = np.genfromtxt(filename, delimiter=',')
    dim = len(data[1,:])
    m = len(data[:, 0])
    X = data[:, [0, dim-2]] if dim > 2 else data[:,0].reshape((m,1)) # Get predictor variable
    X = np.concatenate((np.ones(m).reshape((m,1)), X), axis = 1) # Add a column of ones to x
    y = data[:, [dim-1]]   # Get response variable
    return X, y

def zNormalize(X):
    dim = len(X[0,:])
    mu = np.zeros(((dim-1),1))
    sigma = np.zeros(((dim-1),1))
    for i in range(1, dim):
        mu[i-1] = np.mean(X[:, i])
        sigma[i-1] = np.std(X[:, i])
        X[:, i] = (X[:, i] - mu[i-1]) / sigma[i-1]

    return X, mu, sigma

def computeCost(X, y, theta):
    """
    Function to compute cost (error) for linear regression.

    Using theta as the parameter for linear regression to fit
    the data points in X and y.
    """
    # Initialize some useful values
    m = len(y) # number of training examples

    # vectorized computation of J
    # np commands are a bit of a mess here ... MATLAB would be nicer here.
    #J = 1/(2*m) * np.sum(np.square(np.transpose(np.dot(np.transpose(theta), np.transpose(X)))-y));
    J = 1.0/(2*m) * float(np.dot(np.transpose(np.dot(X, theta)- y), (np.dot(X, theta) - y)))

    return J

def gradientDescent(X, y, theta, alpha, num_iters):
    """
    Function to perform gradient descent to learn theta.
    Iterate of num_iters with liearning rate alpha

    X: Training examples.
    y: Data labels (known values).
    """

    m = len(y); # number of training examples
    J_history = np.zeros((num_iters, 1)); #history of cost
    theta_history  = np.concatenate((theta.reshape((1, len(theta))), np.zeros((num_iters, 2))), axis=0)
    for iter in range(0, num_iters):
        # theta = theta - alpha * 1/m * (((theta'*X')'-y)'*X)'  #MATLAB notation
        #theta = theta - alpha * 1/float(m) * np.transpose(np.dot(np.transpose(np.transpose(np.dot(np.transpose(theta),np.transpose(X)))-y),  X))
        theta = theta - alpha * 1.0/m * np.dot(np.transpose(X), (np.dot(X, theta)-y))

        # Save the cost J in every iteration
        theta_history[iter+1, :] = theta.reshape(2)
        J_history[iter] = computeCost(X, y, theta);

    return theta_history, J_history

def plot_init(title, xlim, ylim, xlabel, ylabel):
    """
    Function to initialize an empty plot with
    with grid lines, a given xrange & yrange,
    axis labels, and graph title.
    """
    fig = plt.figure()
    fig.clf()
    ax = fig.add_subplot(111)
    ax.grid(True, linestyle = '-', color = '0.75')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    return fig

def plot_univariate(X, y, theta, filename):
    """
    Function to plot data (scatter) and regression (line)
    """

    title = "Weight vs. Height Training Data"
    plot_init(title, [min(X[:,1])-0.05*max(X[:,1]), 1.05*max(X[:,1])], [min(y)-0.05*max(y), 1.05*max(y)], "Predictor (z-score)", "Response")
    #plot_init(title, [-5,80], [-250, 250], "Predictor (z-score)", "Response")

    plt.scatter(X[:, 1], y, label="Training Data") # , 'k*', label="Training Data")
    plt.plot(X[:, 1], theta[0] + theta[1] * X[:, 1], color="red", label="Linear Regression Model")
    plt.legend(loc=4)
    plt.savefig( filename, bbox_inches='tight')

def animate_update(num, X, theta, line):
    """
    Function to update the at each iteration.
    """
    line.set_ydata(np.dot(X, theta[num].reshape(2,1)).reshape(len(X[:,1]), 1))   # update the data
    return line,

def animate_results(filename,  X, y, theta, J):
    """
    Function to animate the learning process
    and save the video in a file with filename.
    """
    title = "Linear Regression - Learning Process"
    fig1 = plot_init(title, [min(X[:,1])-0.05*max(X[:,1]), 1.05*max(X[:,1])], [min(y)-0.05*max(y), 1.05*max(y)], "Predictor (z-score)", "Response")

    l, = plt.plot(X[:,1].reshape(len(y),1), np.dot(X, theta[0].reshape(2,1)), 'r-', label="Regression Model")
    plt.scatter(X[:,1], y, label="Training Data")
    plt.legend(loc=4)
    line_ani = animation.FuncAnimation(fig1, animate_update, np.arange(0, len(theta[:,0])), fargs=(X, theta, l),
                                       interval=50, blit=True)
    line_ani.save(filename)




def train_univariate(filename, iter, alpha, normalize, animate):
    """
    Run the regression with single variable.
    """

    # get data and normalize if desired
    X, y = readData(filename)
    if normalize: X, mu, sigma = zNormalize(X)

    # initialize theta parameters
    theta = np.zeros((len(X[0, :]),1))

    # train and return results
    theta_hist, J_hist = gradientDescent(X, y, theta, alpha, iter)

    # print the final parameters and cost
    print "Theta final: ", theta_hist[-1], np.shape(theta_hist)
    print "Final cost: ", J_hist[-1]
    if normalize:
        print "Mean: ", mu
        print "STDEV: ", sigma

    # plot the final results (training data and regression line)
    #plot_univariate(X, y, theta_hist[-1, :], "Foodtruck_normalized.png")

    # animate the process if desired
    if animate: animate_results("Foodtruck_normalized.mp4", X, y, theta_hist, J_hist)

    # return parameters and data
    return X, y, theta_hist[-1, :].reshape((len(X[0, :]), 1))

if __name__ == "__main__":
    # run_univariate(iter, alpha, normalize, animate)
    X, y, theta = train_univariate("weight_height.txt", 1500, 0.01, True, False)
