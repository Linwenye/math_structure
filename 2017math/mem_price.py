# coding=utf-8

import xlrd
import matplotlib.pyplot as plt
import math


def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6378.137  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(
        math.radians(lat2)) * math.sin(dlon / 2) * math.sin(
        dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    return d


# print distance((23.82, 113.96), (23.64, 113.69))
def within(task_place, mem_place):
    defined_distance = 2  # define by ourselves
    if distance(task_place, mem_place) <= defined_distance:
        return True


# the second file reading
filepath = 'C:\Users\Venric\Desktop/two.xlsx'
data = xlrd.open_workbook(filepath)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols

place_mem = []
for i in range(nrows):
    place_mem.append((float(table.row_values(i)[1].split()[0]), float(table.row_values(i)[1].split()[1])))

# the first file reading
filepath_one = 'C:\Users\Venric\Desktop\one.xls'
data_one = xlrd.open_workbook(filepath_one)
table_one = data_one.sheets()[0]
nrows_one = table_one.nrows
ncols_one = table_one.ncols

place_task = []
for i in range(nrows_one):
    place_task.append((table_one.row_values(i)[1], table_one.row_values(i)[2], table_one.row_values(i)[3]))

# compare the two place
# print place_mem
# print place_task
mydict = dict()

mem_price = []
mems = []
price = []
for item in place_task:
    tem = 0

    for i2 in place_mem:
        if within(item[:2], i2):
            tem += 1
    # mems.append(tem)
    # price.append(item[2])
    mem_price.append((tem, item[2]))
    # mydict[(tem, item[2])] = mydict.get((tem, item[2]), 0) + 1
print mem_price
# print mems
# print price

# print mydict.values()
# print mydict.keys()

# mems = [a[0] for a in mydict.keys()]
# price = [a[1] for a in mydict.keys()]
# plt.figure(figsize=(8, 5), dpi=80)
# axes = plt.subplot(111)
#
# type1 = axes.scatter(mems, price, s=[pp*20 for pp in mydict.values()], c='green', marker='o')
#
# plt.show()
