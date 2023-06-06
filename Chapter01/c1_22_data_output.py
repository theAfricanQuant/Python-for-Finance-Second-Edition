# -*- coding: utf-8 -*-
"""
  Name     : c1_22_data_output.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

with open("c:/temp/out.txt","w") as f:
    x="This is great"
    f.write(x)