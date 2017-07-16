matrix = [[0, 6, 3, -1, -1, -1],
          [6, 0, 2, 5, -1, -1],
          [3, 2, 0, 3, 4, -1],
          [-1, 5, 3, 0, 2, 3],
          [-1, -1, 4, 2, 0, 5],
          [-1, -1, -1, 3, 5, 0]]

lenth = len(matrix)
s = [1]
u = [2, 3, 4, 5, 6]
dist = [-1] * 6
dist[0] = 0
mymin = 10000
minnum = None
for i in range(0, lenth):
    if 0 < matrix[0][i] < mymin:
        mymin = matrix[0][i]
        minnum = i + 1
s.append(minnum)
u.remove(minnum)
dist[minnum - 1] = matrix[0][minnum - 1]
while u:
    mymin = 10000
    minnum_tem = -1
    for j in range(0, lenth):
        if matrix[minnum - 1][j] <= 0 or (j+1) in s:
            continue
        newdis = matrix[minnum - 1][j] + dist[minnum - 1]
        if newdis < dist[j] or dist[j] < 0:
            dist[j] = newdis
        if newdis < mymin:
            mymin = newdis
            minnum_tem = j + 1
    minnum = minnum_tem
    u.remove(minnum_tem)
    s.append(minnum_tem)

print dist
