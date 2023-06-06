"""
  Name     : c6_09_save_price_data_from_Google.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import pandas_datareader.data as getData
import re
ticker='msft'
with open("c:/temp/msft.txt","w") as f:
    p = getData.DataReader(ticker, "google")
    f.write(str(p))
