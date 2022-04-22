'''
* 유형
    heap

* 체감 난이도
    ***

'''

import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    works = sorted([-w for w in works])
    heapq.heapify(works)

    for i in range(n):
        a = heapq.heappop(works)
        a += 1
        heapq.heappush(works, a)

    return sum([w * w for w in works])