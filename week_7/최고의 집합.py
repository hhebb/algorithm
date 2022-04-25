'''
* 유형
    단순 구현

* 체감 난이도
    *

'''

def solution(n, s):
    a, b = divmod(s, n)
    if a < 1:
        return [-1]
    answer = [a for i in range(n)]
    for c in range(n-1, n-1-b, -1):
        answer[c] += 1
    return answer