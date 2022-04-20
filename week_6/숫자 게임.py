'''
* 유형
    기교?

* 체감 난이도
    **

* 풀이

'''

def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    a = 0
    b = 0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            a += 1
            b += 1
            answer += 1
        else:
            b += 1
    return answer