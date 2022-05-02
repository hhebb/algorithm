'''
* 유형
    DFS, 트리 후위 탐색
    
* 체감 난이도
    ***

'''

import sys
sys.setrecursionlimit(10 ** 8)

def solution(a, edges):
    global answer
    answer = 0

    graph = {i: [] for i in range(len(a))}
    visited = [False] * len(a)

    for src, dst in edges:
        graph[src].append(dst)
        graph[dst].append(src)

    def recur(node):
        global answer
        visited[node] = True
        for n in graph[node]:
            if not visited[n]:
                recur(n)
                a[node] += a[n]
                answer += abs(a[n])

    recur(0)
    return answer if a[0] == 0 else -1