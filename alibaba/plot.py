#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
工作数和地点
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.read_csv('workLocation.csv', index_col=0)

pd.set_option('display.mpl_style', 'default')  # Make the graphs a bit prettier
font = {'family': 'SimHei',
        'weight': 'bold',
        'size': 8}
mpl.rc('font', **font)
plt.rcParams['figure.figsize'] = (15, 5)
df.sort(columns='工作数').plot(kind='barh')
plt.show()
