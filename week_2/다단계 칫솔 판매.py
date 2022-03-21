'''

* 유형
    구현, 트리

* 체감 난이도
    ***

* 풀이
    1. 판매 기록만큼 루프를 돌면서 꼭대기까지 배분을 해준다.

    배분 금액이 0 원이 되어 절사되면 break 를 걸어서 early stop 해줘야 시간 초과에 걸리지 않음.


'''

def solution(enroll, referral, seller, amount):
    profit = {i:0 for i in enroll}
    enrollRef = {e:r for e, r in zip(enroll, referral)}
    for sel, am in zip(seller, amount):
        am *= 100
        while True:
            rem = am*.1
            if rem < 1:
                remain = 0
                add = am
            else:
                remain = int(rem)
                add = am - remain
            am = remain
            profit[sel] += add
            sel = enrollRef[sel]
            if sel == '-' or am == 0:
                break
    return [profit[e] for e in enroll]