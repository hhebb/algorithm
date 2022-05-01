'''
* 유형
    이분 탐색, 최적화-결정 문제

* 체감 난이도
    ****+
'''

def solution(stones, k):
    l, r = 1, max(stones)

    while l <= r:
        mid = (l + r) // 2

        # 검사
        gap = 0
        exceed = False
        for st in stones:
            if st - mid > 0:
                gap = 0
            else:
                gap += 1

            if gap >= k:
                exceed = True
                break

        if exceed:
            r = mid - 1
        else:
            l = mid + 1

    answer = l
    return answer