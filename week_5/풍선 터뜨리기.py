'''

* 유형
    구현, 메모이제이션

* 체감 난이도
    ****+

* 풀이
    풍선이 살아남으려면?
    해당 풍선 왼쪽에 있는 모든 풍선보다 작거나 오른쪽에 있는 모든 풍선들보다 작거나 혹은 둘 다 작거나
    min, max 함수를 쓰면 시간초과나므로 최대, 최소값을 메모이제이션으로 값을 저장하여 시간을 줄인다.

'''

def solution(a):
    if len(a) <= 2:
        return 2

    answer = 0
    left, right = a[0], a[-1]

    for i in range(len(a)):
        if a[i] < left:
            left = a[i]
            answer += 1
        if a[len(a) - i - 1] < right:
            right = a[len(a) - i - 1]
            answer += 1

    answer += 1
    return answer