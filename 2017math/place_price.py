# coding=utf-8

import xlrd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filepath = 'C:\Users\Venric\Desktop\one.xls'
data = xlrd.open_workbook(filepath)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols


def place_with_label():
    place_unfinished_x = []
    place_unfinished_y = []
    price_unfinished = []
    place_done_x = []
    place_done_y = []
    price_done = []
    for i in range(nrows):
        if table.row_values(i)[4] == 0:
            place_unfinished_x.append(table.row_values(i)[1])
            place_unfinished_y.append(table.row_values(i)[2])
            price_unfinished.append(table.row_values(i)[3])
        else:
            place_done_x.append(table.row_values(i)[1])
            place_done_y.append(table.row_values(i)[2])
            price_done.append(table.row_values(i)[3])

    fig = plt.figure(figsize=(8, 5), dpi=80)
    axes = fig.add_subplot(111, projection='3d')
    type1 = axes.scatter(place_done_y, place_done_x, price_done, s=40, c='green', marker='+')
    type2 = axes.scatter(place_unfinished_y, place_unfinished_x, price_unfinished, s=20, c='black', marker='o')
    axes.legend((type1, type2), (u'finished', u'unfinished'), loc=2)

    plt.show()


def place_nolabel():
    place_x = []
    place_y = []
    price = []
    for i in range(nrows):
        place_x.append(table.row_values(i)[1])
        place_y.append(table.row_values(i)[2])
        price.append(table.row_values(i)[3])

    fig = plt.figure(figsize=(8, 5), dpi=80)
    axes = fig.add_subplot(111, projection='3d')
    axes.scatter(place_y, place_x, price, s=40, c='green', marker='+')
    plt.show()


def plot_2d():
    place_x = []
    place_y = []
    price = []
    for i in range(nrows):
        place_x.append(table.row_values(i)[1])
        place_y.append(table.row_values(i)[2])
        price.append(table.row_values(i)[3])

    fig = plt.figure(figsize=(8, 5), dpi=80)
    axes = fig.add_subplot(111)
    axes.scatter(place_y, place_x, s=[(i-64)*8 for i in price], c='green', marker='s')
    plt.show()


place_nolabel()
place_with_label()
plot_2d()
