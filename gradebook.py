"""
Practicing pandas by manipulating gradebook.
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('play.csv')

col_names = ['last', 'first', 'id', 'nothing', 'last_acess', 'avail', 'weight_total', 'total', 'hw1', 'hw2', 'hw3', 'hw4', 'hw5', 'hw6', 'midterm1', 'hw7', 'midterm1_redo', 'hw8', 'hw9', 'midterm2', 'hw10', 'hw11', 'midterm2_redo', 'hw12', 'hw13', 'hw14']

df.columns = col_names

df2 = df.replace(np.NaN, 0)

df2[['last', 'first', 'midterm1', 'midterm1_redo', 'mid1_redo_diff']]
df2['mid1_redo_diff'] = df2.midterm1 - df2.midterm1_redo

df2['mid1_redo_diff_2'] = df2[['midterm1', 'midterm1_redo']].max(axis=1)

hw = ['hw{}'.format(n) for n in range(1, 15)]
df2[hw]
df2['hw'] = df2[hw].sum(axis=1)
df2[['last', 'first', 'hw']]

people = df2.to_dict(orient='records')
s = '{first} {last} got {midterm1} on Midterm1'

for person in people:
    print(s.format(**person))


s = (
'{first} {last}:\n'
'\tMidterm1: {midterm1}\n'
'\tMidterm2: {midterm2}\n'
'\tHW: {hw}\n'
)

for person in people:
    print(s.format(**person))
