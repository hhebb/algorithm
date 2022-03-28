'''
* 유형
    DP, 그래프 탐색

* 체감 난이도
    ****

* 풀이
    재귀적으로 그래프를 탐색하며 최소 비용을 구해야 함.
    단순히 재귀를 돌리면 시간초과.
    가지치기(prunning) 와 DP 를 추가하여 중복과 경우의 수를 줄였다.
        재귀를 돌 때마다 현재 비용이 최소 비용보다 커지면 가망이 없으므로 무조건 조기 종료
        각 블럭에 도착했을 때 비용이 그 블럭에 도달하는 데 소요되는 비용보다 크면 이미 최소 비용이 될 수 없으므로 조기 종료.


    def recur(r, c, move_direction, cost):
        1.
        DT[r][c] >= cost 이면 DT[r][c] = cost
        아니면 조기 종료.

        2.
        min_cost < cost 이면 조기 종료.

        3.
        도착지에 도착하면 min_cost 업데이트

        for direc in range(4):

            4.
            맵을 벗어나거나 벽을 만나면 무효.

            5.
            이전 이동방향 (move_direction), 현재 이동방향 (direc) 을 비교해 직진인지 꺾는건지 판단한다.
            alpha = 직진이면 100, 코너이면 100+500

            visit[r][c] = True
            recur(next_r, next_c, direc, cost+alpha)
            visit[r][c] = False

'''


dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def solution(board):
    dt = [[10 ** 9] * len(row) for row in board]
    visited = [[False] * len(row) for row in board]
    visited[0][0] = True

    global min_cost
    min_cost = 10 ** 9

    def recur(r, c, orient, cost):
        global min_cost

        # 해당 블럭까지 가는데 비용보다 현재 비용이 크면 조기 종료
        if dt[r][c] >= cost:
            dt[r][c] = cost
        else:
            return

        # 현재 비용이 최소 비용보다 이미 커지면 미리 조기 종료
        # !! 이 코드는 없어도 되지만 있으면 시간이 더 줄어듬!!
        if cost > min_cost:
            return

        # 도착지에 도착하면 최소 비용 업데이트
        if (r == len(board) - 1 and c == len(board) - 1) and cost < min_cost:
            if cost < min_cost:
                min_cost = cost
            return

        for d in range(4):
            next_r, next_c = r + dr[d], c + dc[d]
            o = 1 if d in [1, 3] else 0  # [1, 3] 이면 가로(1), [0, 2] 면 세로(0).

            # 직진이면 100, 코너이면 100 + 500 추가
            if (orient % 2 == 1 and o % 2 == 1) or (orient % 2 == 0 and o % 2 == 0) or orient == -1:
                alpha = 100
            else:
                alpha = 600

            # 맵을 벗어나면 무효
            if not (0 <= next_r < len(board) and 0 <= next_c < len(board)):
                continue

            # 벽을 만나면 무효
            if board[next_r][next_c] == 1:
                continue

            # 재귀
            if not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                recur(next_r, next_c, o, cost + alpha)
                visited[next_r][next_c] = False

    recur(0, 0, -1, 0)
    return min_cost