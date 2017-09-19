# coding=utf-8

import xlrd
import matplotlib.pyplot as plt
import numpy as np
from geopy.geocoders import Nominatim

# the first file reading
filepath_one = 'C:\Users\Venric\Desktop/newdata.xls'
data_one = xlrd.open_workbook(filepath_one)
table_one = data_one.sheets()[0]
nrows_one = table_one.nrows
ncols_one = table_one.ncols

geo = Nominatim()

res = []
pp = 0
for i in range(nrows_one):
    pp += 1
    if pp < 2025:
        continue
    # res.append(geo.reverse(','.join(table.row_values(i)[1].split())))
    print geo.reverse(str(table_one.row_values(i)[1]) + ',' + str(table_one.row_values(i)[2])).address

# print res
# plt.figure(figsize=(8, 5), dpi=80)
# axes = plt.subplot(111)
# type1 = axes.scatter(place_y, place_x, s=30, c='green', marker='o')
#
# plt.xlim(112.58215813092218, 114.59831928531567)
# plt.ylim(22.412523531090759, 23.958957660369446)
# plt.show()
