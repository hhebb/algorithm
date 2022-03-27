'''
* 유형
    최단거리, 다익스트라

* 체감 난이도
    ***

* 풀이
    1. 특정 지점까지 무조건 동승했을 때 최단거리
    2. 그 이후에 각자 집으로 갈 때 각 최단거리
    3. 이들을 다 합쳤을때 최소가 되는 값을 찾는다.

    [S, A, B] 3 지점에 대해서 다익스트라를 돌려서 가지고 있는다.
    함께 동승할 지점에 대해서 반복문을 돌리며 그 지점에서 [S, A, B] 에 대한 각 최소거리를 더하면 됨.

    all-to-all 최단거리를 뽑아내는 플로이드 와샬 알고리즘을 사용할 수도 있지만
    다익스트라는 3 번만 돌리면 되므로 다익스트라를 사용했음.

'''

from heapq import heappop, heappush
def solution(n, s, a, b, fares):
    graph = {i: {} for i in range(1, n+1)}
    for site1, site2, f in fares:
        graph[site1][site2] = f
        graph[site2][site1] = f

    def dijkstra(s):
        h = [(0, s)]
        min_dists = {node: 10**9 if node != s else 0 for node in graph}
        while len(h) > 0:
            dist, here = heappop(h)
            for there, d in graph[here].items():
                new_dist = min_dists[here] + graph[here][there]
                if min_dists[there] > new_dist:
                    min_dists[there] = new_dist
                    heappush(h, (new_dist, there))
        return min_dists

    d_start, d_a, d_b = dijkstra(s), dijkstra(a), dijkstra(b)
    return min([d_start[node] + d_a[node] + d_b[node] for node in range(1, n+1)])