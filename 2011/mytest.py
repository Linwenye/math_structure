# encoding=utf-8

matrix = [[0, 6, 3, -1, -1, -1],
          [6, 0, 2, 5, -1, -1],
          [3, 2, 0, 3, 4, -1],
          [-1, 5, 3, 0, 2, 3],
          [-1, -1, 4, 2, 0, 5],
          [-1, -1, -1, 3, 5, 0]]

lenth = len(matrix)
for ii in range(0, lenth):
    s = [ii + 1]
    u = range(1, lenth + 1)
    u.remove(ii + 1)
    dist = [-1] * lenth
    dist[ii] = 0
    mymin = 1000000
    minnum = None
    for t in range(0, lenth):
        if matrix[ii][t] <= 0:
            continue

        dist[t] = matrix[ii][t]

        if matrix[ii][t] < mymin:
            mymin = matrix[ii][t]
            minnum = t + 1
    s.append(minnum)
    u.remove(minnum)
    dist[minnum - 1] = matrix[ii][minnum - 1]
    while u:
        mymin = 1000000
        minnum_tem = -1
        for j in range(0, lenth):
            if matrix[minnum - 1][j] <= 0 or (j + 1) in s:
                continue
            newdis = matrix[minnum - 1][j] + dist[minnum - 1]
            if newdis < dist[j] or dist[j] < 0:
                dist[j] = newdis
            if newdis < mymin:
                mymin = newdis
                minnum_tem = j + 1

        for j in range(0, lenth):
            if 0 < dist[j] < mymin and (j+1) in u:
                mymin = dist[j]
                minnum_tem = j + 1

        # if minnum_tem == -1:  # 剩下的不存在了
        #     break

        minnum = minnum_tem
        u.remove(minnum_tem)
        s.append(minnum_tem)
    print dist
