'''
* 유형
    구간합

* 체감 난이도
    ****
'''

def solution(board, skill):
    cumulated = [[0] * (len(board[0]) + 1) for row in range(len(board) + 1)]
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            cumulated[r1][c1] -= degree
            cumulated[r1][c2 + 1] += degree
            cumulated[r2 + 1][c1] += degree
            cumulated[r2 + 1][c2 + 1] -= degree
        elif t == 2:
            cumulated[r1][c1] += degree
            cumulated[r1][c2 + 1] -= degree
            cumulated[r2 + 1][c1] -= degree
            cumulated[r2 + 1][c2 + 1] += degree

    for r in range(len(board)):
        for c in range(1, len(board[0])):
            cumulated[r][c] += cumulated[r][c - 1]

    for c in range(len(board[0])):
        for r in range(1, len(board)):
            cumulated[r][c] += cumulated[r - 1][c]

    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += cumulated[r][c]

    c = [len(list(filter(lambda x: x > 0, row))) for row in board]
    return sum(c)