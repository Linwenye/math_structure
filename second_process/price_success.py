# coding=utf-8

import xlrd
import matplotlib.pyplot as plt
import numpy as np

filepath = 'C:\Users\Venric\Desktop\one.xls'
data = xlrd.open_workbook(filepath)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols

price_unfinished = []
price_done = []
for i in range(nrows):
    # print table.row_values(i)
    if table.row_values(i)[4] == 0:
        price_unfinished.append(table.row_values(i)[3])
    else:
        price_done.append(table.row_values(i)[3])
print price_done
print price_unfinished
print min(min(price_done), min(price_unfinished))
print max(max(price_done), max(price_unfinished))

successls = [0] * 10
faills = [0] * 10

for num in price_done:
    for i in range(0, 10):
        if 65 + i * 2 <= num < 67 + i * 2 or (i == 9 and num == 85):
            successls[i] += 1

for num in price_unfinished:
    for i in range(0, 10):
        if 65 + i * 2 <= num < 67 + i * 2 or (i == 9 and num == 85):
            faills[i] += 1

print successls
print faills

fig, ax = plt.subplots()
index = np.arange(10)
bar_width = 0.35

opacity = 0.4
rects1 = plt.bar(index, successls, bar_width, alpha=opacity, color='b', label='success price')
rects2 = plt.bar(index + bar_width, faills, bar_width, alpha=opacity, color='r', label='fail price')

plt.xlabel('Price')
plt.ylabel('Nums')
plt.title('Price and success')
plt.xticks(index + bar_width, ['~'.join([str(65 + 2 * p), str(67 + 2 * p)]) for p in range(0, 10)])
plt.ylim(0, 200)
plt.legend()

plt.tight_layout()
plt.show()
