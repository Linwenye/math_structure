# coding=utf-8
import json
import numpy
import xlrd

filepath = 'C:\Users\Venric\Desktop\data1.xls'
data = xlrd.open_workbook(filepath)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols

city_price_dict = {}
for i in range(nrows):
    city_name = (table.row_values(i)[5])[3:5]
    if city_name not in city_price_dict.keys():
        city_price_dict[city_name] = []
    city_price_dict[city_name].append(table.row_values(i)[3])

for kk in city_price_dict.items():
    print json.dumps(kk, encoding='utf-8', ensure_ascii=False)
    print numpy.average(kk[1])
print json.dumps(city_price_dict, encoding="UTF-8", ensure_ascii=False)
