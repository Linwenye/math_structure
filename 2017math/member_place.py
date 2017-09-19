# coding=utf-8

import xlrd
import matplotlib.pyplot as plt
import numpy as np

filepath = 'C:\Users\Venric\Desktop/two.xlsx'
data = xlrd.open_workbook(filepath)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols

place_x = []
place_y = []
for i in range(nrows):
    place_x.append(table.row_values(i)[1].split()[0])
    place_y.append(table.row_values(i)[1].split()[1])

print place_x
print place_y
plt.figure(figsize=(8, 5), dpi=80)
axes = plt.subplot(111)
type1 = axes.scatter(place_y, place_x, s=30, c='green', marker='o')
plt.xlim(112.58215813092218, 114.59831928531567)
plt.ylim(22.412523531090759, 23.958957660369446)
plt.show()
