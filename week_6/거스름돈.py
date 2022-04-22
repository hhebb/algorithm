'''
* 유형
    DP

* 체감 난이도
    ****
'''

def solution(n, money):
    DT = [0] * (n + 1)
    DT[0] = 1

    for m in money:
        for c in range(1, n + 1):
            if c - m >= 0:
                print(f'{c} 원 만드는데 {c - m} 사용')
                DT[c] += DT[c - m]
            print(DT)

    return DT[-1] % 1000000007