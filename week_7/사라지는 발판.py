'''
* 유형
    백트랙, 게임 이론

* 체감 난이도
    ****+

'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, M = 0, 0


def B_turn(curboard, A, B, turn):
    x, y = B
    if curboard[x][y] == 0:
        return (-1, turn)
    flag = False
    winner = []
    loser = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if curboard[nx][ny] == 1:
                new_board = [row[:] for row in curboard]
                new_board[x][y] = 0
                iswin, new_turn = A_turn(new_board, A, (nx, ny), turn + 1)
                if iswin == -1:
                    winner.append(new_turn)
                else:
                    loser.append(new_turn)
                flag = True
    if flag:
        if winner:
            return (1, min(winner))
        else:
            return (-1, max(loser))
    else:
        return (-1, turn)


def A_turn(curboard, A, B, turn):
    x, y = A
    if curboard[x][y] == 0:
        return (-1, turn)
    flag = False
    winner = []
    loser = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if curboard[nx][ny] == 1:
                new_board = [row[:] for row in curboard]
                new_board[x][y] = 0
                iswin, new_turn = B_turn(new_board, (nx, ny), B, turn + 1)
                if iswin == -1:
                    winner.append(new_turn)
                else:
                    loser.append(new_turn)
                flag = True
    if flag:
        if winner:
            return (1, min(winner))
        else:
            return (-1, max(loser))
    else:
        return (-1, turn)


def solution(board, aloc, bloc):
    global N, M
    N = len(board)
    M = len(board[0])

    return A_turn(board, aloc, bloc, 0)[1]

# dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
# case = {0: 'a', 1: 'b'}
# rolls = {'a':{0: 'chase', 1: 'flee'}, 'b':{0: 'flee', 1: 'chase'}}

# def solution(board, aloc, bloc):
#     global game_board
#     global answer
#     global answer_2
#     game_board = board
#     answer = 10**9
#     answer_2 = 0

#     # 둘이 만나지 못하는 경우
#     check = [[False]*len(board[0]) for r in range(len(board))]
#     def floodfill(r, c):
#         if board[r][c] == 0:
#             return False

#         check[r][c] = True
#         ret = True

#         for d in range(4):
#             r2, c2 = r+dr[d], c+dc[d]
#             if 0 <= r2 < len(board) and 0 <= c2 < len(board[0]):
#                 if not check[r2][c2]:
#                     floodfill(r2, c2)

#         return ret

#     chunk = 0
#     for r in range(len(board)):
#         for c in range(len(board[0])):
#             if not check[r][c]:
#                 chunk += floodfill(r, c)
#     # print('chunk', chunk)

#     # 현재 위치에서 움직일 수 있는 방향들의 리스트를 반환
#     def movableDirec(ra, ca, rb, cb, roll):
#         global game_board
#         dirs = {}

#         # 상하좌우 전부 0 이거나 맵 밖이거나 본인 자리가 0 이 되었거나
#         if game_board[ra][ca] == 0:
#             dirs = {}
#         else:
#             for d in range(4):
#                 r2, c2 = ra+dr[d], ca+dc[d]
#                 if not (0 <= r2 < len(board) and 0 <= c2 < len(board[0])):
#                     continue

#                 if game_board[r2][c2] == 0:
#                     continue

#                 dist = abs(r2-rb) + abs(c2-cb)
#                 dirs[d] = dist

#         if roll == 'chase':
#             try:
#                 minDist = min(dirs.items(), key=lambda x:x[1])[1]
#                 direc = [k for k, v in dirs.items() if v == minDist]
#             except Exception as e:
#                 direc = []
#         elif roll == 'flee':
#             try:
#                 maxDist = max(dirs.items(), key=lambda x:x[1])[1]
#                 direc = [k for k, v in dirs.items() if v == maxDist]
#             except:
#                 direc = []
#         # print('direc', direc, dirs)
#         return direc

#     def recur(pos_a, pos_b, order, move_count, cc):
#         global game_board
#         global answer
#         global answer_2
#         # for gb in game_board:
#         #     print(gb)
#         # print(pos_a, pos_b)
#         # print('')

#         if order == 'a':
#             dirs = movableDirec(*pos_a, *pos_b, rolls[case[cc]][0])
#             if len(dirs) == 0:
#                 # if cc == 0:
#                 #     print('reset', order)
#                 #     return
#                 # print('over', order, move_count)
#                 answer = min(answer, move_count)
#                 answer_2 = max(answer_2, move_count)
#                 return
#             r, c = pos_a
#             game_board[r][c] = 0
#             for d in dirs:
#                 r2, c2 = r+dr[d], c+dc[d]
#                 recur((r2, c2), pos_b, 'b', move_count+1, cc)
#             game_board[r][c] = 1
#         elif order == 'b':
#             dirs = movableDirec(*pos_b, *pos_a, rolls[case[cc]][1])
#             if len(dirs) == 0:
#                 # if cc == 1:
#                 #     print('reset', order)
#                 #     return
#                 # print('over', order, move_count)
#                 answer = min(answer, move_count)
#                 answer_2 = max(answer_2, move_count)
#                 return
#             r, c = pos_b
#             game_board[r][c] = 0
#             for d in dirs:
#                 r2, c2 = r+dr[d], c+dc[d]
#                 recur(pos_a, (r2, c2), 'a', move_count+1, cc)
#             game_board[r][c] = 1


#     recur(aloc, bloc, 'a', 0, 0)
#     # print('change')
#     recur(aloc, bloc, 'a', 0, 1)
#     # print(answer, answer_2)
#     return answer if chunk == 1 else answer_2