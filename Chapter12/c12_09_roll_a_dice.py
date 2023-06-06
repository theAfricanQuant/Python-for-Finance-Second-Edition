"""
  Name     : c12_09_roll_a_dice.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import random
def rollDice():
    return random.randint(1,6)
n=10
random.seed(123)
result = [rollDice() for _ in range(1, n)]
print(result)