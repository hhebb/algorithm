'''

* 유형
    탐색, 순열 조합

* 체감 난이도
    ****

* 풀이

    * 재귀
    처음에 재귀함수를 이용해 친구들을 배치하는 알고리즘을 작성함.
    런타임 에러 (재귀 depth 초과) 가 계속 발생함.
    가지치기를 해줘도 해결 안됨.


    * 순열 이용
    permutation 으로 경우의 수를 뽑아서 친구들을 배치함.
    레스토랑 외벽을 2 배로 늘려 선형으로 만들면 친구들 배치하기 쉬워짐.


'''


###############################
# 순열 이용
###############################

from itertools import permutations

def solution(n, weak, dist):
    used = []
    weak_point = weak + [w + n for w in weak]

    for i, start in enumerate(weak):
        for order in permutations(dist):
            count = 1
            position = start
            for o in order:
                position += o
                if position < weak_point[i + len(weak) - 1]:
                    count += 1
                    position = [w for w in weak_point[i + 1:i + len(weak)] if w > position][0]
                else:
                    used.append(count)
                    break

    return min(used) if used else -1


###############################
# 원래 풀이. 재귀. 런타임 에러
###############################


import sys
sys.setrecursionlimit(10 ** 9)

def solution(n, weak, dist):
    global answer
    global weak_points
    answer = 10 ** 9
    dist = dist[::-1]
    weak_points = weak

    def recur(d_i, start):
        global weak_points
        global answer

        # 가지치기
        if d_i >= answer - 1:
            return

        if d_i != -1:
            # 처리
            cover = [p % n for p in range(start, start + dist[d_i] + 1)]
            weak_points = [w for w in weak_points if w not in cover]
        weak_copy = weak_points[:]

        # 출구
        if len(weak_points) == 0 or d_i == len(dist):
            if d_i < answer:
                answer = d_i + 1
            return

        # 탐색
        for w in weak_points:
            recur(d_i + 1, w)
            weak_points = weak_copy.copy()

    recur(-1, None)
    return answer