'''
* 유형
    그리디, MST, 크루스칼

* 체감 난이도
    ***

'''

def solution(n, costs):
    answer = 0
    nodes = set()
    for a, b, c in costs:
        nodes.add(a)
        nodes.add(b)

    parents = {i: i for i in nodes}
    costs = sorted(costs, key=lambda x: x[2])

    def union(a, b):
        pa, pb = find(a), find(b)
        if pa > pb:
            parents[pa] = b
        else:
            parents[pb] = a

    def find(node):
        if parents[node] != node:
            parents[node] = find(parents[node])
        return parents[node]

    for a, b, c in costs:
        if find(a) != find(b):
            union(a, b)
            answer += c
    return answer

# def solution(n, costs):
#     costs = sorted(costs, key=lambda x:x[2])
#     node = set([costs[0][0], costs[0][1]])
#     answer = costs[0][2]

#     while len(node) != n:
#         for i in range(1, len(costs)):
#             if costs[i][0] in node and costs[i][1] in node:
#                 continue
#             if costs[i][0] in node or costs[i][1] in node:
#                 node.update([costs[i][0], costs[i][1]])
#                 answer += costs[i][2]
#                 break
#     return answer