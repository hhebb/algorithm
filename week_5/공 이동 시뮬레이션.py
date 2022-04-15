'''
* 유형
    구현

* 체감 난이도
    ****

* 풀이
    아이디어
    1. 쿼리를 도착점에서 역순으로 돌린다.
        그러면 쿼리를 돌려서 도착점에 도달가능한 영역이 직사각형으로 나온다.
    2. 세로 방향, 가로 방향 이동은 서로 독립이라 각각 따로 고려해준다.
    3. matrix 를 넘어가는 부분만 추가적으로 잘 처리해준다.
    4. 도달가능 영역의 면적을 구한다.

    ############################

    아이디어 1, 2 는 생각해냈지만 풀이로는 이어지지 못해서 답안을 참조함.
    그냥 여러번 풀면서 감을 익히는게 맞는듯?

'''


def solution(n, m, x, y, queries):
    answer = 0
    t, l, r, b = x, y, y, x
    queries.reverse()
    for i, j in queries:
        if i == 0:
            if r + j < m:
                tmp = r + j
            else:
                tmp = m - 1
            if l == 0:
                r = tmp
            else:
                l, r = l + j, tmp
        if i == 1:
            if l - j >= 0:
                tmp = l - j
            else:
                tmp = 0
            if r == m - 1:
                l = tmp
            else:
                l, r = tmp, r - j
        if i == 2:
            if b + j < n:
                tmp = b + j
            else:
                tmp = n - 1
            if t == 0:
                b = tmp
            else:
                t, b = t + j, tmp
        if i == 3:
            if t - j >= 0:
                tmp = t - j
            else:
                tmp = 0
            if b == n - 1:
                t = tmp
            else:
                t, b = tmp, b - j
        if l > m - 1 or r < 0 or t > n - 1 or b < 0:
            break
        print(t, b, l, r)

    else:
        answer = ((b - t) + 1) * ((r - l) + 1)
    return answer