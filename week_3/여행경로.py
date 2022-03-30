'''
* 유형
    DFS, 스택

* 체감 난이도
    ***+

* 풀이
    처음에 단순히 DFS 돌리면 되는 줄 알고 풀었는데 2 번 테스트케이스에서 계속 런타임 에러가 남.
    디버깅 결과, 모든 티켓을 다 사용하지도 못하고 종료가 되었음.
    예외상황을 발견하지 못하여, 풀이를 참조함.

    - 일반적인 DFS 처럼 재귀적으로 탐색을 한다.
    - visited 배열을 사용하지 않고 edge 를 끊어버려도 방문 여부를 체크할 수 있다.
    - 재귀 함수 마지막에 연결된 edge 가 없으면 answer 에 기록한다.
    - 이 문제는 요약하면, 탐색은 흔히 하던것처럼 하되 어떻게 기록을 하느냐가 관건임.


'''

from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)

    for src, dst in tickets:
        graph[src].append(dst)

    for g, l in graph.items():
        graph[g] = sorted(l)

    def dfs(node):
        while graph[node]:
            dfs(graph[node].pop(0))

        if len(graph[node]) == 0:
            answer.append(node)

    dfs('ICN')
    return answer[::-1]