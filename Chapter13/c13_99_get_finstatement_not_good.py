"""
  Name     : c13_99_get_finstatement.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 2/27/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import re,sys
import requests
from bs4 import BeautifulSoup

url='https://finance.yahoo.com/quote/AAPL/financials?ltr=1'
#url = "https://finance.yahoo.com/q/is?s=AAPL&annual"
#html = requests.get(url).content
#soup = BeautifulSoup(html)
x=BeautifulSoup(requests.get(url).text, "html.parser")




def getFin(ticker, statement="IS", quarterly=False):
    if statement in ["is", "bs", "cf"]:
        url = f"https://finance.yahoo.com/q/{statement}?s={ticker}"
        if not quarterly:
            url += "&annual"
        return BeautifulSoup(requests.get(url).text, "html.parser")
    return sys.exit(f"Invalid financial statement code '{statement}' passed.")
#
#x=getFin("AAPL")


