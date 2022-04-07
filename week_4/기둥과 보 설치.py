'''
* 유형
    빡구현

* 체감 난이도
    ****+

* 풀이
    1. 해당 좌표에 있는 구조물이 합당한 상태인지 판단하는 judge 함수 작성.
    2. 설치할 때 - 일단 해당 위치에 구조물을 설치해보고, judge 함수가 True 이면 그대로 놓고, False 이면 다시 물린다.
    3. 제거할 때 - 일단 해당 위치의 구조물을 제거해보고, judge 함수가 False 이면 다시 돌려놓는다.
        하나의 구조물을 제거하면 최대 3 단위거리까지 파급효과가 미칠 수 있음.
        이 경우를 모두 조사하는 건 너무 복잡해지므로, 단순 반복으로 모든 경우를 조사하여 한 곳에서라도 judge 가 False 나면 다시 돌려놓는다.


    -------------------------------

    최대 구조물이 1000 개 이하이므로 완전 탐색을 써도 큰 문제는 없어보임.
    처음에 단순히 조건문으로만 처리하려고 했는데 디버깅이 지옥 수준으로 올라갔음.
    시간이 너무 오래 걸려서 힌트를 보고 코드를 작성함.

    구조물 설치는 큰 문제가 되지 않는데, 제거할 때 매우 복잡해짐.
    일단 모든 경우를 따진 후 제거할 지 결정하는 것 보다,
    '먼저 제거를 한 후 그 상태가 올바른지 확인' 하는 것이 빠르게 풀 수 있는 '핵심 포인트' 인 듯.


'''


def solution(n, build_frame):
    def judge(x, y, kind):
        if kind == 0:
            if not ((y == 0) or (beam[x][y] or beam[x - 1][y]) or (pillar[x][y - 1])):
                return False
        elif kind == 1:
            if not ((pillar[x][y - 1] or pillar[x + 1][y - 1]) or (beam[x - 1][y] and beam[x + 1][y])):
                return False
        return True

    pillar = [[False] * (n + 1) for i in range(n + 1)]
    beam = [[False] * (n + 1) for i in range(n + 1)]

    for x, y, kind, command in build_frame:
        if command == 1:
            if kind == 0:
                pillar[x][y] = True
                if not judge(x, y, kind):
                    pillar[x][y] = False
            elif kind == 1:
                beam[x][y] = True
                if not judge(x, y, kind):
                    beam[x][y] = False

        elif command == 0:
            if kind == 0:
                pillar[x][y] = False
            else:
                beam[x][y] = False

            check = True
            for xx in range(n + 1):
                for yy in range(n + 1):
                    if (pillar[xx][yy] and not judge(xx, yy, 0)) or (beam[xx][yy] and not judge(xx, yy, 1)):
                        check = False
                        break
                if not check:
                    break
            if not check:
                if kind == 0:
                    pillar[x][y] = True
                else:
                    beam[x][y] = True

    result = []
    for x in range(n + 1):
        for y in range(n + 1):
            result.append([x, y, 0]) if pillar[x][y] else None
            result.append([x, y, 1]) if beam[x][y] else None
    return sorted(result)