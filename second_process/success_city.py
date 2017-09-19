# coding=utf-8
import json

import xlrd
import read_mem

filepath = 'C:\Users\Venric\Desktop\data1.xls'
data = xlrd.open_workbook(filepath)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols

city_success_dict = {}
city_fail_dict = {}
for i in range(nrows):
    city_name = (table.row_values(i)[5])[3:5]
    district_name = (table.row_values(i)[5])[6:8]
    if table.row_values(i)[4] == 0:
        if city_name not in city_fail_dict.keys():
            city_fail_dict[city_name] = dict()
        city_fail_dict[city_name][district_name] = city_fail_dict[city_name].get(district_name, 0) + 1
    else:
        if city_name not in city_success_dict.keys():
            city_success_dict[city_name] = dict()
        city_success_dict[city_name][district_name] = city_success_dict[city_name].get(district_name, 0) + 1

print json.dumps(city_fail_dict, encoding="UTF-8", ensure_ascii=False)
print json.dumps(city_success_dict, encoding="UTF-8", ensure_ascii=False)
print json.dumps(read_mem.task_location, encoding="UTF-8", ensure_ascii=False)

dict_shenzhen = {}
dict_foshan = {}
dict_guangzhou = {}


def outfunc(city_str, the_dict):
    for pp, gg in read_mem.task_location[city_str].items():
        success_rate = city_success_dict[city_str].get(pp, 0) / float(
            city_fail_dict[city_str].get(pp, 0) + city_success_dict[city_str].get(pp, 0))
        print city_str, pp, 'success rate:', round(success_rate, 4), 'price:', gg
        the_dict[pp] = (gg, round(success_rate, 4) * 100)


outfunc(u'深圳', dict_shenzhen)
outfunc(u'佛山', dict_foshan)
outfunc(u'广州', dict_guangzhou)

print dict_foshan
