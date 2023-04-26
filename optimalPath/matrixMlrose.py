def mlroseform(m):
    l = []
    for i in range(len(m)):
        for j in range(len(m)):
            if (m[i][j] > 0):
                l.append((i,j,m[i][j]))
    return l

a = [[0,2,3],[4,0,8],[2,5,0]]

mlroseform(a)