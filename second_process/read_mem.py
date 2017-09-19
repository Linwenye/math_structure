# coding=utf-8
import xlrd
import json
import numpy


def mymean(lst):
    my_lst = lst
    original = numpy.average(lst)
    for a_price in my_lst:
        if abs(a_price - original) >= 9:
            my_lst.remove(a_price)
    return numpy.average(my_lst)


def filter_word(word):
    word = word.strip()
    if word.find('(') >= 0:
        word = word[:word.find('(')].strip()
    if word.endswith(u'区'):
        word = word[:-1]
    return word


def read_to_dict(city_str, member_place):
    if city_str in member_place:
        temls = memberplace.split(',')
        for ii, item_in in enumerate(temls):
            if city_str in item_in:
                district = filter_word(temls[ii - 1])
                if city_str not in city_member_dict.keys():
                    city_member_dict[city_str] = {}
                city_member_dict[city_str][district] = city_member_dict[city_str].get(district, 0) + 1


# the second file reading
filepath = 'C:\Users\Venric\Desktop/two.xlsx'
data = xlrd.open_workbook(filepath)
table = data.sheets()[0]

city_member_dict = {}
citystr_tuple = (u'佛山市 / Foshan', u'广州市 / Guangzhou', u'深圳市 / Shenzhen', u'东莞市 / Dongguan')
for i in range(table.nrows):
    row = table.row_values(i)
    memberplace = row[5]
    for cityitem in citystr_tuple:
        if cityitem in memberplace:
            read_to_dict(cityitem, memberplace)
# print json.dumps(city_member_dict, encoding='utf-8', ensure_ascii=False)

# the task location
filepath = 'C:\Users\Venric\Desktop\data1.xls'
data = xlrd.open_workbook(filepath)
table = data.sheets()[0]

task_location = dict()
for i in range(table.nrows):
    city_name = (table.row_values(i)[5])[3:5]
    district_name = ''
    if table.row_values(i)[6]:
        if u'龙岗' in table.row_values(i)[6]:
            district_name = u'龙岗'
            city_name = u'深圳'
        for tt, item in enumerate(table.row_values(i)[6].split(',')):
            if u'东莞市 / Dongguan' in item:
                district_name = filter_word(table.row_values(i)[6].split(',')[tt - 1])
    else:
        district_name = (table.row_values(i)[5])[6:8]

    if city_name not in task_location.keys():
        task_location[city_name] = dict()
    if district_name not in task_location[city_name].keys():
        task_location[city_name][district_name] = []
    task_location[city_name][district_name].append(table.row_values(i)[3])

# print json.dumps(task_location, encoding='utf-8', ensure_ascii=False)
for x, y in task_location.items():
    for p, q in y.items():
        task_location[x][p] = round(mymean(q), 2)
# print json.dumps(task_location, encoding='utf-8', ensure_ascii=False)
# print json.dumps(task_location.keys(), encoding='utf-8', ensure_ascii=False)
# print json.dumps(city_member_dict.keys(), encoding='utf-8', ensure_ascii=False)

# for x, y in task_location.items():
#     for p, q in y.items():
#
#         for temtem in citystr_tuple:
#             if x in temtem and (p in city_member_dict[temtem].keys()):
#                 for dddd in q:
#                     print city_member_dict[temtem][p],dddd
