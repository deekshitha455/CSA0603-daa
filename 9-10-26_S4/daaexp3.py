def champagneTower(poured, query_row, query_glass):
    tower = [[0.0] * (i + 1) for i in range(101)]
    tower[0][0] = poured
    for i in range(100):
        for j in range(i + 1):
            if tower[i][j] > 1:
                excess = (tower[i][j] - 1) / 2
                tower[i + 1][j] += excess
                tower[i + 1][j + 1] += excess
    return min(1.0, tower[query_row][query_glass])
poured = int(input())
query_row = int(input())
query_glass = int(input())
result = champagneTower(poured, query_row, query_glass)
print("%.5f" % result)