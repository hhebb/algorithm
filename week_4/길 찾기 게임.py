'''

* 유형
    트리, 트리 탐색, 구현

* 체감 난이도
    ***+

* 풀이
    1. 트리 구성하기
        1.1. nodeinfo 를 y 값 기준 내림차순, x 값 기준 오름차순으로 정렬. (가장 앞의 info 가 root)
        1.2. 재귀적으로
        1.3. 남은 node 들 중 y 값이 가장 큰 값을 가진 것들 중 root 보다 큰 것을 root 의 right, 작은 것을 root 의 left 로 지정한다.
        1.3. root 보다 큰 값들, 작은 값들을 나누며 재귀적으로 트리를 구성한다.
    2. 트리 순회하기
        2.1. 간단하게 dfs 로 전위탐색과 후위탐색을 동시에 진행한다.

'''


import sys
sys.setrecursionlimit(10 ** 9)


class Node:
    def __init__(self, right, left, x, y):
        self.right = right
        self.left = left
        self.x = x
        self.y = y


def solution(nodeinfo):
    tree = {tuple(nodeinfo[i]): {'node': Node(None, None, *nodeinfo[i]), 'idx': i + 1} for i in range(len(nodeinfo))}
    nodeinfo = sorted(nodeinfo, key=lambda x: (x[1], -x[0]), reverse=True)
    root = nodeinfo[0]

    # 트리 구성
    def recur(x, y, nodes):
        if len(nodes) == 0:
            return

        level = max(nodes, key=lambda x: x[1])[1]
        left = None
        right = None
        while len(nodes) > 0:
            if nodes[0][1] == level:
                pop = nodes.pop(0)
                if pop[0] > x:
                    right = pop
                else:
                    left = pop
            else:
                break
        tree[(x, y)]['node'].left = left
        tree[(x, y)]['node'].right = right

        left_side = list(filter(lambda v: x > v[0], nodes))
        right_side = list(filter(lambda v: x < v[0], nodes))

        recur(*left, left_side) if left else None
        recur(*right, right_side) if right else None

    recur(*root, nodeinfo[1:])

    # 트리 탐색
    pre = []
    post = []

    def traverse(root_info):
        if not root_info:
            return

        root_node = tree[tuple(root_info)]['node']

        left = root_node.left
        right = root_node.right

        pre.append(tree[tuple(root_info)]['idx'])
        traverse(left)
        traverse(right)
        post.append(tree[tuple(root_info)]['idx'])

    traverse(root)
    return [pre, post]