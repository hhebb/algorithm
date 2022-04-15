'''

* 유형
    BFS, 구현

* 체감 난이도
    ****+

* 풀이
    아이디어
    1. 일반적인 grid 에서의 BFS 인데 노드마다 상하좌우 이동의 4 가지의 edge 가 아니라, 회전 4 가지가 추가된 8 개의 edge 를 가짐.
    2. 함수를 하나 만들어 8 개의 edge 중 가능한 edge (가능한 이동 및 회전) 들을 반환하도록 함.
    3. 그 이후엔 일반적인 BFS 알고리즘을 돌리면 됨.

    matrix 외벽을 1 로 둘러싸면 범위를 벗어나는 움직임을 아주 깔끔하게 해결가능함.

    ex)
    111111
    1    1
    1    1
    111111

    #########################################

    회전 처리하는게 너무 어렵다고 생각했음.
    조건문 쓰다가 지쳐서 답안 참조함.
    회전 처리 부분 없으면 일반적인 BFS.
    matrix 외벽 처리는 다른 문제에서도 유용하게 쓰일듯!!


'''


from collections import deque

def can_move(cur1, cur2, new_board):
    Y, X = 0, 1
    cand = []
    # 평행이동
    DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dy, dx in DELTAS:
        nxt1 = (cur1[Y] + dy, cur1[X] + dx)
        nxt2 = (cur2[Y] + dy, cur2[X] + dx)
        if new_board[nxt1[Y]][nxt1[X]] == 0 and new_board[nxt2[Y]][nxt2[X]] == 0:
            cand.append((nxt1, nxt2))
    # 회전
    if cur1[Y] == cur2[Y]:  # 가로방향 일 때
        UP, DOWN = -1, 1
        for d in [UP, DOWN]:
            if new_board[cur1[Y] + d][cur1[X]] == 0 and new_board[cur2[Y] + d][cur2[X]] == 0:
                cand.append((cur1, (cur1[Y] + d, cur1[X])))
                cand.append((cur2, (cur2[Y] + d, cur2[X])))
    else:  # 세로 방향 일 때
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if new_board[cur1[Y]][cur1[X] + d] == 0 and new_board[cur2[Y]][cur2[X] + d] == 0:
                cand.append(((cur1[Y], cur1[X] + d), cur1))
                cand.append(((cur2[Y], cur2[X] + d), cur2))

    return cand


def solution(board):
    # board 외벽 둘러싸기
    N = len(board)
    new_board = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]

    # 현재 좌표 위치 큐 삽입, 확인용 set
    que = deque([((1, 1), (1, 2), 0)])
    confirm = set([((1, 1), (1, 2))])

    while que:
        cur1, cur2, count = que.popleft()
        if cur1 == (N, N) or cur2 == (N, N):
            return count
        for nxt in can_move(cur1, cur2, new_board):
            if nxt not in confirm:
                que.append((*nxt, count + 1))
                confirm.add(nxt)