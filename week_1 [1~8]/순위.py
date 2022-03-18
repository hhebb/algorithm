'''
* 유형
    그래프, 탐색

* 체감 난이도
    **+

* 풀이
    특정 선수의 순위가 확정되려면 그 선수가 이긴 횟수, 진 횟수를 더했을 때 총 인원 - 1 이 되어야 한다.

    주어진 정보로 정방향, 역방향 그래프를 각각 구현한다.
    그래프를 탐색하면 이긴(진) 선수들의 목록을 구할 수 있다.
    선수 한 명에 대해 정, 역 방향 그래프를 탐색하며 counting 을 하여 그 수가 총 인원 -1 이면 답에 추가한다.

'''


def solution(n, results):
    answer = 0
    graph = {i + 1: [] for i in range(n)}
    graph_inv = {i + 1: [] for i in range(n)}
    global count
    count = 0

    for a, b in results:
        graph[a].append(b)
        graph_inv[b].append(a)

    # 정방향 그래프
    def dfs(node):
        global count
        check[node] = True
        count += 1
        for there in graph[node]:
            dfs(there) if not check[there] else None

    # 역방향 그래프
    def dfs2(node):
        global count
        check[node] = True
        count += 1
        for there in graph_inv[node]:
            dfs2(there) if not check[there] else None

    # 각 선수들에 대해서 순위 확정 판단
    for i in range(1, n + 1):
        count = 0
        check = {j: False for j in range(1, n + 1)}
        dfs(i)

        # check 초기화 해줌
        check = {j: False for j in range(1, n + 1)}
        dfs2(i)

        if count - 1 == n:
            answer += 1
    return answer