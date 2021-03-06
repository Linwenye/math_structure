# encoding=utf-8
"""最短寻路"""
import json


class Point:
    def __init__(self, num, x, y, is_platform):
        self.num = num
        self.x = x
        self.y = y
        self.is_platform = is_platform
        self.min = None
        self.platform = None

    def get_distance(self, ano_point):
        return ((ano_point.x - self.x) ** 2 + (ano_point.y - self.y) ** 2) ** 0.5


class Graph:
    def __init__(self, matrix, vertex_list):
        self.matrix = matrix
        self.vertex_list = vertex_list
        self.shortest_path = []
        self.shortest()

    def shortest(self):
        lenth = len(self.matrix)
        for ii in range(0, lenth):
            s = [ii + 1]
            u = range(1, lenth + 1)
            u.remove(ii + 1)
            dist = [-1] * lenth
            dist[ii] = 0
            mymin = 1000000
            minnum = None

            # 直接连接的点
            for t in range(0, lenth):
                if self.matrix[ii][t] <= 0:
                    continue

                dist[t] = self.matrix[ii][t]

                if self.matrix[ii][t] < mymin:
                    mymin = self.matrix[ii][t]
                    minnum = t + 1
            s.append(minnum)
            u.remove(minnum)
            dist[minnum - 1] = self.matrix[ii][minnum - 1]

            # 间接连接
            while u:
                mymin = 1000000
                minnum_tem = -1
                for j in range(0, lenth):
                    if self.matrix[minnum - 1][j] <= 0 or (j + 1) in s:
                        continue
                    newdis = self.matrix[minnum - 1][j] + dist[minnum - 1]
                    if newdis < dist[j] or dist[j] < 0:
                        dist[j] = newdis
                    if newdis < mymin:
                        mymin = newdis
                        minnum_tem = j + 1

                for j in range(0, lenth):
                    if 0 < dist[j] < mymin and (j + 1) in u:
                        mymin = dist[j]
                        minnum_tem = j + 1

                minnum = minnum_tem
                u.remove(minnum_tem)
                s.append(minnum_tem)

            self.shortest_path.append(dist)


# 数据初始化
a_x = [413, 403, 383.5, 381, 339, 335, 317, 334.5, 333, 282, 247, 219, 225, 280, 290, 337, 415, 432, 418, 444, 251, 234,
       225, 212, 227, 256, 250.5, 243, 246, 314, 315, 326, 327, 328, 336, 336, 331, 371, 371, 388.5, 411, 419, 411, 394,
       342, 342, 325, 315, 342, 345, 348.5, 351, 348, 370, 371, 354, 363, 357, 351, 369, 335, 381, 391, 392, 395, 398,
       401, 405, 410, 408, 415, 418, 422, 418.5, 405.5, 405, 409, 417, 420, 424, 438, 438.5, 434, 438, 440, 447, 448,
       444.5, 441, 440.5, 445, 444]
a_y = [359, 343, 351, 377.5, 376, 383, 362, 353.5, 342, 325, 301, 316, 270, 292, 335, 328, 335, 371, 374, 394, 277, 271,
       265, 290, 300, 301, 306, 328, 337, 367, 351, 355, 350, 342.5, 339, 334, 335, 330, 333, 330.5, 327.5, 344, 343,
       346, 342, 348, 372, 374, 372, 382, 380.5, 377, 369, 363, 353, 374, 382.5, 387, 382, 388, 395, 381, 375, 366, 361,
       362, 359, 360, 355, 350, 351, 347, 354, 356, 364.5, 368, 370, 364, 370, 372, 368, 373, 376, 385, 392, 392, 381,
       383, 385, 381.5, 380, 360]
path_from = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9, 10, 11, 11, 12, 12, 14, 15, 15, 16, 16, 17, 17, 17, 18, 18,
             19, 20, 21, 22, 22, 23, 23, 24, 24, 25, 26, 26, 27, 28, 28, 29, 30, 30, 31, 31, 32, 33, 33, 34, 35, 36, 36,
             36, 36, 37, 38, 38, 39, 40, 41, 41, 42, 43, 43, 44, 45, 46, 46, 47, 47, 47, 48, 49, 49, 50, 51, 51, 52, 53,
             53, 54, 54, 55, 56, 57, 57, 57, 58, 60, 61, 62, 62, 63, 64, 64, 65, 66, 66, 67, 67, 68, 68, 69, 69, 69, 70,
             70, 71, 71, 72, 73, 73, 74, 74, 75, 76, 77, 77, 78, 79, 80, 81, 82, 82, 83, 84, 85, 86, 86, 87, 87, 88, 88,
             89, 89, 89, 90, 91]
path_to = [75, 78, 44, 45, 65, 39, 63, 49, 50, 59, 32, 47, 9, 47, 35, 34, 22, 26, 25, 471, 21, 7, 31, 14, 38, 40, 42,
           81, 81, 83, 79, 86, 22, 372, 13, 13, 383, 13, 25, 11, 27, 10, 12, 29, 15, 30, 7, 48, 32, 34, 33, 34, 8, 9,
           45, 35, 37, 16, 39, 7, 39, 41, 40, 2, 17, 92, 43, 2, 72, 3, 46, 8, 55, 48, 6, 5, 61, 50, 53, 51, 52, 59, 56,
           52, 54, 55, 63, 3, 57, 58, 60, 4, 59, 62, 60, 4, 85, 64, 65, 76, 66, 67, 76, 44, 68, 69, 75, 70, 71, 1, 2,
           43, 72, 74, 73, 74, 18, 1, 80, 76, 77, 78, 19, 79, 80, 18, 82, 83, 90, 84, 85, 20, 87, 88, 88, 92, 89, 91,
           20, 84, 90, 91, 92]

# 建立顶点信息
_vertex_list = []
_num = 1
for _x, _y in zip(a_x, a_y):
    if _num <= 20:
        _vertex_list.append(Point(_num, _x, _y, True))
    else:
        _vertex_list.append(Point(_num, _x, _y, False))
    _num += 1

# 邻接矩阵初始化  92*92
_matrix = []
for _ in range(0, 92):
    _matrix.append([-1] * 92)
for i in range(0, 92):
    _matrix[i][i] = 0

# 建立边信息
for _f, _t in zip(path_from, path_to):
    if _t > 92:
        continue
    else:
        distance = _vertex_list[_f - 1].get_distance(_vertex_list[_t - 1])
        _matrix[_f - 1][_t - 1] = distance
        _matrix[_t - 1][_f - 1] = distance

graph = Graph(_matrix, _vertex_list)
# print graph.shortest_path

res_dict = dict()
for _j in range(1, 21):
    res_dict['平台' + str(_j)] = []

longest_res = []
for _f, _t in zip(path_from, path_to):
    if _t > 92:
        continue
    else:
        shortest1 = 1000000
        short_num1 = -1
        shortest2 = 1000000
        short_num2 = -1
        for pp in range(0, 20):
            if graph.shortest_path[_f - 1][pp] < shortest1:
                shortest1 = graph.shortest_path[_f - 1][pp]
                short_num1 = pp + 1
            if graph.shortest_path[_t - 1][pp] < shortest2:
                shortest2 = graph.shortest_path[_t - 1][pp]
                short_num2 = pp + 1

    _distance = _vertex_list[_f - 1].get_distance(_vertex_list[_t - 1])
    sum_distance = round((shortest1 + shortest2 + _distance) / 2 * 100, 2)
    # longest_res.append((sum_distance, (a_x[_f - 1] + a_x[_t - 1]) / 2, (a_y[_f - 1] + a_y[_t - 1]) / 2))
    pre_dis = round((sum_distance - shortest1) * 100, 2)
    bac_dis = round(_distance * 100 - pre_dis, 2)

    if short_num1 == short_num2:
        res_dict['平台' + str(short_num1)].append('节点{} 到节点{}'.format(_f, _t))
        # print '节点{} 到节点{} 由平台{}管理'.format(_f, _t, short_num1)

    elif a_x[_f - 1] < a_x[_t - 1]:
        res_dict['平台' + str(short_num1)].append('节点{}到节点{}前{}米'.format(_f, _t, pre_dis))
        res_dict['平台' + str(short_num2)].append('节点{}到节点{}后{}米'.format(_f, _t, bac_dis))
        # print '节点{} 到节点{} 前{} 米由平台{}管理，后{} 米由平台{}管理'.format(_f, _t, pre_dis, short_num1, bac_dis, short_num2)
    else:
        res_dict['平台' + str(short_num1)].append('节点{}到节点{}前{}米'.format(_f, _t, pre_dis))
        res_dict['平台' + str(short_num2)].append('节点{}到节点{}后{}米'.format(_f, _t, bac_dis))
        # print '节点{} 到节点{} 前{} 米由平台{}管理，后{} 米由平台{}管理'.format(_f, _t, bac_dis, short_num2, pre_dis, short_num1)

    if _f == 3 and _t == 45:
        print short_num1, shortest1
        print short_num2, shortest2
        print _distance*100
        print
print sorted(longest_res)
# print json.dumps(sorted([e for e in res_dict.items()]), encoding="UTF-8", ensure_ascii=False)
# print json.dumps(res_dict, encoding="UTF-8", ensure_ascii=False)
