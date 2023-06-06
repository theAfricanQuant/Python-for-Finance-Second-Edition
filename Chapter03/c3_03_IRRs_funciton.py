# -*- coding: utf-8 -*-
"""
  Name     : c3_03_IRRs_funciton.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import numpy as sp
cashflows=[55,-50,-50,-50,100]
n=1000
n_cashflow=len(cashflows)
epsilon=sp.abs(sp.mean(cashflows))*0.01
irr=[-99.00]
lag_sign=sp.sign(sp.npv(0,cashflows))
j=1
for i in range(1, n + 1):
    interest=i*0.001
    s=sp.sign(sp.npv(interest,cashflows))
    if s*lag_sign<0:
        lag_sign=s
        if j==1:
            irr=[interest]
            j=2
        else:
            irr.append(interest)
            
            
            
   
        