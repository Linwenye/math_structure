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


def within(task_place, mem_place, defined_distance):
    # defined_distance = 0.02  # define by ourselves
    if distance(task_place, mem_place) <= defined_distance:
        return True


def file_read_location(path_str):
    data_one = xlrd.open_workbook(path_str)
    table_one = data_one.sheets()[0]
    nrows_one = table_one.nrows

    task_locate = []
    for i in range(nrows_one):
        task_locate.append((table_one.row_values(i)[1], table_one.row_values(i)[2]))

    return task_locate


def task_file_reading():
    # the first file reading
    filepath_one = 'C:\Users\Venric\Desktop\one.xls'
    return file_read_location(filepath_one)

if __name__ == '__main__':

    # testlst = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65]
    testlst = range(2, 21)
    place_task = file_read_location('C:\Users\Venric\Desktop/newdata.xls')

    for test in [p / 20.0 for p in testlst]:

        mem_price = []
        mems = []
        price = []
        check1 = 0
        check2 = 0
        check3 = 0
        check4 = 0
        # place_task = task_file_reading()
        for item in place_task:
            tem = 0

            for i2 in place_task:
                if within(item[:2], i2, test):
                    tem += 1
            mem_price.append(tem)
            if tem == 1:
                check1 += 1
            elif tem == 2:
                check2 += 1
            elif tem == 3:
                check3 += 1
            elif tem == 4:
                check4 += 1

        # print mem_price
        print test, round(check1 / float(len(mem_price)) * 100,2), \
            round(check2 / float(len(mem_price)) * 100,2),\
            round(check3 / float(len(mem_price)) * 100,2),\
            round(check4 / float(len(mem_price)) * 100,2)
