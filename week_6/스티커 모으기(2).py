'''
* 유형
    DP

* 체감 난이도
    ****

* 풀이

'''

def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)

    dt1 = [0] * len(sticker)
    dt2 = [0] * len(sticker)

    dt1[0] = sticker[0]
    dt1[1] = dt1[0]
    dt1[2] = dt1[0] + sticker[2]

    dt2[0] = 0
    dt2[1] = sticker[1]
    dt2[2] = dt2[1]

    for i in range(2, len(sticker) - 1):
        dt1[i] = max(dt1[i - 2] + sticker[i], dt1[i - 3] + sticker[i])

    for i in range(2, len(sticker)):
        dt2[i] = max(dt2[i - 2] + sticker[i], dt2[i - 3] + sticker[i])

    return max(max(dt1), max(dt2))