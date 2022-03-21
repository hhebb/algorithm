'''
* 유형
    투 포인터

* 체감 난이도
    **+

* 풀이
    단순 리스트 반복을 하면 (O(N^2)) 시간초과가 발생함.
    구간 탐색에 효율적인 투 포인터 알고리즘으로 한 칸 씩 긁으며 검사한다.
        모든 종류의 보석이 최소 하나씩이라도 있으면 start 포인터를 1 늘림
        그렇지 않으면 end 포인터를 1 늘림

    모든 종류의 보석이 최소 하나씩있음을 판단하기 위해 변수를 하나 생성해야 효율적으로 알고리즘이 작동함.

'''

def solution(gems):
    kind = set(gems)
    bag = {k: 0 for k in kind}
    bag[gems[0]] = 1
    cart = []
    start, end = 0, 0
    zeros = len(kind) - 1

    while end < len(gems):
        if zeros > 0: # min(bag.values()) == 0 을 쓰면 시간초과가 발생함.
            end += 1
            if end < len(gems):
                bag[gems[end]] += 1
                if bag[gems[end]] == 1:
                    zeros -= 1 # 하나도 없는 보석 종류가 줄어듬
        else:
            cart.append((start, end))
            bag[gems[start]] -= 1
            if bag[gems[start]] == 0:
                zeros += 1 # 하나도 없는 보석 종류가 늘어남
            start += 1

    tmp = sorted([[b - a, a, b] for a, b in cart])
    return [tmp[0][1] + 1, tmp[0][2] + 1]