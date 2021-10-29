'''
Created on 2021/10/29

@author: t19cs027
'''
import random

a = random.randint(0,2)
b = random.randint(0,2)

if a == 0:
    if b == 0:
        print('Aの手：グー v.s. Bの手：グー → 引き分け')
    elif b == 1:
        print('Aの手：グー v.s. Bの手：チョキ → Aの勝ち')
    else:
        print('Aの手：グー v.s. Bの手：パー → Bの勝ち')
elif a == 1:
    if b == 0:
        print('Aの手：チョキ v.s. Bの手：グー → Bの勝ち')
    elif b == 1:
        print('Aの手：チョキ v.s. Bの手：チョキ → 引き分け')
    else:
        print('Aの手：チョキ v.s. Bの手：パー → Aの勝ち')
else:
    if b == 0:
        print('Aの手：パー v.s. Bの手：グー → Aの勝ち')
    elif b == 1:
        print('Aの手：パー v.s. Bの手：チョキ → Bの勝ち')
    else:
        print('Aの手：パー v.s. Bの手：パー → 引き分け')