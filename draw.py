import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import matplotlib as mpl
import pandas as pd
s = "数据矩阵"
a = s.split(' ')
city1 = []
city2 = []
city3 = []
for i in range(len(a)):
    a[i] = int(float(a[i]))
for i in range(len(a)):
    if i % 3 == 0:
        city1.append(a[i])
    elif i % 3 == 1:
        city2.append(a[i])
    else:
        city3.append(a[i])
x = np.arange(1,51,1)
plt.plot(x, city3)
plt.show()
