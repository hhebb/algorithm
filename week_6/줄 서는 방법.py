'''
* 유형
    절차적 풀이, 구현

* 체감 난이도
    **

'''

from math import ceil
from functools import reduce

def solution(n, k):
    answer = []
    people = list(range(1, n + 1))
    fac = reduce(lambda x, y: x * y, range(1, n + 1))

    for i, pos in enumerate(range(n, 1, -1)):
        fac //= pos
        a = ceil(k / fac) - 1
        answer.append(people[a])
        k -= a * fac
        people.pop(a)
    answer.append(people[0])
    return answer