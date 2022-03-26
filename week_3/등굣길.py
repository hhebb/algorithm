'''
* 유형
    DP

* 체감 난이도
    **

* 풀이
    점화식
    DT[r][c] = DT[r][c-1] + DT[r-1][c]
        (DT[r][c] = 0 | 물웅덩이에 해당하는 곳)

    초딩 때 써먹던 경로 경우의 수 테크닉을 쓰면
    첫 번째 행과 첫 번째 열에서 물웅덩이가 나올 때 오답이 나옴. (1행과 1 열은 무조건 1 로 채우는 방식)
    1 행과 1 열도 점화식에 맞춰서 채워줘야 함.


'''

def solution(m, n, puddles):
    dt = [[0 for c in range(m)] for r in range(n)]
    dt[0][0] = 1

    for r in range(n):
        for c in range(m):
            if r == 0:
                if [c + 1, r + 1] not in puddles:
                    dt[r][c] += dt[r][c - 1]
            elif c == 0:
                if [c + 1, r + 1] not in puddles:
                    dt[r][c] += dt[r - 1][c]
            else:
                if [c + 1, r + 1] not in puddles:
                    dt[r][c] = dt[r][c - 1] + dt[r - 1][c]

    return dt[-1][-1] % 1000000007