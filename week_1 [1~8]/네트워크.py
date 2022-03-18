'''

* 유형
    DFS, BFS

* 체감 난이도
    *

* 풀이
    모든 노드에 대해 그래프 탐색을 실시하면 몇 개의 연결된 덩어리가 나오는지 알 수 있음.

    이미 방문이 된 노드는 그 노드로부터 탐색을 할 이유가 없으므로 넘어가고
    방문이 안 된 노드만 탐색을 하며 체크를 해주면 연결된 네트워크를 모두 체크할 수 있다.


'''


def solution(n, computers):
    answer = 0
    graph = {com+1:[] for com in range(n)}
    [[graph[v1+1].append(v2+1) if conn == 1 and v1!=v2 else None for v2, conn in enumerate(l)] for v1, l in enumerate(computers)]
    check = {i+1:False for i in range(len(computers))}

    def dfs(here):
        check[here] = True
        [dfs(there) if not check[there] else None for there in graph[here]]

    for v in graph:
        if not check[v]:
            answer += 1
            dfs(v)
    return answer