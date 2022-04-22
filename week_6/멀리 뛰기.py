'''
* 유형
    DP

* 체감 난이도
    **

'''

def solution(n):
    a, b = 1, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b % 1234567