'''
* 유형
    전처리, 최단거리, BFS

* 체감 난이도
    **+

* 풀이
    1. 각 단어를 node 로 하고, 각 단어마다 철자가 하나씩만 다른 node 를 edge 로 연결한 그래프를 생성한다. (전처리)
    2. start node 로 부터 BFS 로 탐색하며 각 node 까지 거리를 기록한다.
        처음 target node 를 방문한 시점에서 그 거리를 반환한다.


    - target node 까지 닿을 수 없으면 처음부터 불가능하다고 처리함.
    - 이동은 words 에 있는 node 끼리만 가능하고 `start node` 로는 다시 돌아올 수 없으므로 그래프 구성할 때 주의함.


'''

def solution(begin, target, words):
    # 불가능한 경우 걸러내기
    if target not in words:
        return 0

    # 전처리
    pool = [[begin, []]]
    pool.extend([word, []] for word in words)
    for i in range(len(pool)):
        for j in range(i + 1, len(pool)):
            match = [a == b for a, b in zip(pool[i][0], pool[j][0])]
            if sum(match) == len(begin) - 1:
                pool[i][1].append(pool[j][0])
                pool[j][1].append(pool[i][0]) if i != 0 else None
    pool = dict(pool)

    # bfs
    check = {p: False if p != begin else True for p in pool}
    q = [begin]
    dists = {p: 0 for p in pool}
    while len(q) > 0:
        here = q.pop(0)
        for there in pool[here]:
            if not check[there]:
                dists[there] = dists[here] + 1
                if there == target:
                    return dists[target]
                check[there] = True
                q.append(there)