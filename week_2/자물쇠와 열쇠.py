'''
* 유형
    빡구현

* 체감 난이도
    ****

* 풀이
    1. 열쇠 4 방향 회전
    2. 열쇠를 좌상단에서부터 우하단까지 쭉 슬라이딩하며 겹치는 부분 검사
    3. 자물쇠와 열쇠가 겹치는 부분의 합이 각각 모두 1 이면서 자물쇠 안 겹치는 부분이 모두 1 이라면 가능.

    처음부터 열려있는 자물쇠가 있을 수 있음.

'''

def solution(key, lock):
    key_copy = key.copy()

    for rot in range(4):
        # 90 도 회전
        key_copy = list(zip(*key_copy))[::-1]

        for i in range(len(key) + len(lock) + 1):
            for j in range(len(key) + len(lock) + 1):

                # 겹칠 부분 지정
                if i < len(key):
                    srRange = (len(key) - i, len(key))
                    drRange = (0, i)
                elif len(key) <= i < len(lock):
                    srRange = (0, len(key))
                    drRange = (i - len(key), i)
                elif i >= len(lock):
                    srRange = (0, len(key) + len(lock) - i)
                    drRange = (i - len(key), len(lock))

                if j < len(key):
                    scRange = (len(key) - j, len(key))
                    dcRange = (0, j)
                elif len(key) <= j < len(lock):
                    scRange = (0, len(key))
                    dcRange = (j - len(key), j)
                elif j >= len(lock):
                    scRange = (0, len(key) + len(lock) - j)
                    dcRange = (j - len(key), len(lock))

                # 열쇠, 자물쇠 겹치는 부분 flatten
                k = [row[scRange[0]:scRange[1]] for row in key_copy[srRange[0]:srRange[1]]]
                l = [row[dcRange[0]:dcRange[1]] for row in lock[drRange[0]:drRange[1]]]

                # 열쇠와 완전히 겹치는가?
                a_flat = []
                b_flat = []
                for a, b in zip(k, l):
                    [a_flat.append(aa) for aa in a]
                    [b_flat.append(bb) for bb in b]

                match = False
                for a, b in zip(a_flat, b_flat):
                    if a + b != 1:
                        break
                else:
                    match = True

                if not match:
                    continue

                # 겹치는 부분이 딱 맞다면, 겹치지 않는 부분은 모두 1 인가?
                match = True
                for r in range(len(lock)):
                    for c in range(len(lock)):
                        if r not in range(drRange[0], drRange[1]) or c not in range(dcRange[0], dcRange[1]):
                            if lock[r][c] != 1:
                                match = False
                                break
                    if not match:
                        break

                if match:
                    return True
    return False