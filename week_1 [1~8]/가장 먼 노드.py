'''

* 유형
    그래프 최단거리, 다익스트라

* 체감 난이도
    *+

* 풀이
    1 번 노드에서 각 노드까지 최단거리를 구해서 그 중 최대값을 가지는 노드가 몇 개인지 구한다.

    한 노드에서 나머지 모든 노드까지 최단거리를 구할 수 있는 다익스트라 알고리즘으로 최단거리 리스트를 뽑는다.
    최단 거리 리스트에서 최대값을 찾고, 그 값을 가지는 원소 갯수를 구한다.

* 기타
    Counter 모듈 이용하면 최단거리의 최댓값과 그 갯수를 바로 알 수 있음.
    다익스트라는 heap 을 이용하면 더 효율적으로 동작한다.

'''


from heapq import heappush, heappop
from collections import Counter
def solution(n, edge):
    graph = {i+1:[] for i in range(n)}
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    minDists = {i+1:1e9 if i!=0 else 0 for i in range(n)}
    q = [(1e9, 1)]
    while len(q) > 0:
        minDist, here = heappop(q)
        for there in graph[here]:
            if minDists[there] > minDists[here] + 1:
                minDists[there] = minDists[here] + 1
                heappush(q, (minDists[there], there))
    c = Counter([dist for k, dist in minDists.items()])
    return max(c.items(), key=lambda x:x[0])[1]