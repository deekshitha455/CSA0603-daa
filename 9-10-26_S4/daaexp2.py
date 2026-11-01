def gameOfLife(board):
    m = len(board)
    n = len(board[0])
    new_board = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            live = 0
            for x in range(max(0, i-1), min(m, i+2)):
                for y in range(max(0, j-1), min(n, j+2)):
                    if (x, y) != (i, j):
                        live += board[x][y]
            if board[i][j] == 1:
                if live == 2 or live == 3:
                    new_board[i][j] = 1
            else:
                if live == 3:
                    new_board[i][j] = 1
    return new_board
m, n = map(int, input().split())
board = []
for i in range(m):
    row = list(map(int, input().split()))
    board.append(row)
result = gameOfLife(board)
print(result)