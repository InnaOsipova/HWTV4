# Дополнительно (на повторение)
# Даны значения зарплат из выборки выпускников:

# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.

# построить гистограмму распределения, подобрав лучший параметр bins,
# найти первый и третий квартили, интерквартильное расстояние. Найти выбросы в выборке, используя для этого "усы" из boxplot.

import matplotlib.pyplot as plt
#import seaborn as sns

sellary  = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
sellary.sort()

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import seaborn
#passing the histogram function n, bins, 
patches = plt.hist(sellary, 30, histtype='bar', density=True, facecolor='yellow', alpha=0.80) 
plt.xlabel('Значения') 
plt.ylabel('Плотность') 
plt.title('Гистограмма зарплат выпускников') 
plt.xlim(0, 180) 
plt.ylim(0, 0.04) 
plt.grid(True) 
plt.show()

q1 = np.quantile(sellary, .25)
print("Первый квартиль : ", q1) 
q3 = np.quantile(sellary, .75)
print("Третий квартиль : ", q3) 
iq = q3 - q1
print("Межквартильное растояние : ", iq) 

max = q3+(1.5*iq)
min = q1-(1.5*iq)
print('Выбросы ')
for i in sellary:
    if i < min or i > max:
        print (i)

 
boxplot = seaborn.boxplot(data=sellary)
plt.show()