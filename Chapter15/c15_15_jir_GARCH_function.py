"""
  Name     : c15_15_GARCH_function.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from matplotlib.mlab import csv2rec
from scipy.optimize import fmin_slsqp 
from numpy import size, log, pi, sum, diff, array, zeros, diag, dot, mat, asarray, sqrt
#
def gjr_garch_likelihood(parameters, data, sigma2, out=None): 
    mu = parameters[0]
    omega = parameters[1]
    alpha = parameters[2]
    gamma = parameters[3]
    beta = parameters[4]
    T = size(data,0)
    eps = data-mu
    for t in xrange(1,T):
        sigma2[t]=(omega+alpha*eps[t-1]**2+gamma*eps[t-1]**2*(eps[t- 1]<0)+beta*sigma2[t-1])
        logliks = 0.5*(log(2*pi) + log(sigma2) + eps**2/sigma2)
    loglik = sum(logliks)
    return loglik if out is None else (loglik, logliks, copy(sigma2))
#
def gjr_constraint(parameters,data, sigma2, out=None):
    alpha = parameters[2]
    gamma = parameters[3] 
    beta = parameters[4]
    return array([1-alpha-gamma/2-beta]) # Constraint alpha+gamma/2+beta<=1
#
def hessian_2sided(fun, theta, args): 
    f = fun(theta, *args)
    h = 1e-5*np.abs(theta) 
    thetah = theta + h
    h = thetah-theta 
    K = size(theta,0) 
    h = np.diag(h)
    fp = zeros(K) 
    fm = zeros(K)
    for i in xrange(K):
        fp[i] = fun(theta+h[i], *args) 
        fm[i] = fun(theta-h[i], *args)
        fpp = zeros((K,K))
        fmm = zeros((K,K)) 
    for i in xrange(K):
        for j in xrange(i,K):
            fpp[i,j] = fun(theta + h[i] + h[j], *args) 
            fpp[j,i] = fpp[i,j]
            fmm[i,j] = fun(theta-h[i]-h[j], *args) 
            fmm[j,i] = fmm[i,j]
            hh = (diag(h))
            hh = hh.reshape((K,1))
            hh = dot(hh,hh.T)
            H = zeros((K,K)) 
    for i in xrange(K):
        for j in xrange(i,K):
            H[i,j] = (fpp[i,j]-fp[i]-fp[j] + f+ f-fm[i]-fm[j] + fmm[i,j])/hh[i,j]/2
            H[j,i] = H[i,j]
    return H
