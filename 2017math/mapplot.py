# coding=utf-8

import xlrd
import matplotlib.pyplot as plt
import numpy as np

filepath = 'C:\Users\Venric\Desktop\one.xls'
data = xlrd.open_workbook(filepath)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols

place_unfinished_x = []
place_unfinished_y = []
place_done_x = []
place_done_y = []
for i in range(nrows):
    if table.row_values(i)[4] == 0:
        place_unfinished_x.append(table.row_values(i)[1])
        place_unfinished_y.append(table.row_values(i)[2])
    else:
        place_done_x.append(table.row_values(i)[1])
        place_done_y.append(table.row_values(i)[2])

print place_done_x
print place_done_y

print place_unfinished_x
print place_unfinished_y
# print place_done
# print place_unfinished
#
plt.figure(figsize=(8, 5), dpi=80)
axes = plt.subplot(111)
#
type1 = axes.scatter(place_done_y, place_done_x, s=40, c='green', marker='+')
type2 = axes.scatter(place_unfinished_y, place_unfinished_x, s=20, c='black', marker='o')
# # plt.scatter(matrix[:, 0], matrix[:, 1], s=20 * numpy.array(labels),
# #             c=50 * numpy.array(labels), marker='o',
# #             label='test')
# plt.xlabel(u'x')
# plt.ylabel(u'y')
axes.legend((type1, type2), (u'successfully finished', u'unfinished'), loc=2)

plt.show()
