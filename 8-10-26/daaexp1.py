m = 2
n = 2
N = 2
i = 0
j = 0

dp = [[0] * n for _ in range(m)]
dp[i][j] = 1

count = 0

for step in range(N):
    temp = [[0] * n for _ in range(m)]

    for r in range(m):
        for c in range(n):
            if dp[r][c] > 0:
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        count += dp[r][c]
                    else:
                        temp[nr][nc] += dp[r][c]

    dp = temp

print(count)