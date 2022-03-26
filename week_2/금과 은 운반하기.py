'''

* 유형
    결정 문제, 이분 탐색

* 체감 난이도
    ****

* 풀이
    광물을 모두 운반하는데 걸리는 최적(최소)의 시간이 얼마인지 찾는 문제를
    특정 시간이 광물을 모두 운반하는데 걸리는 최적의 시간이 맞는지 찾는 문제로 바꿈.
    전형적인 `최적화 문제 --> 결정 문제` 유형.
    1 주차 때의 `입국 심사` 문제와 같은 유형.
    시간을 0 부터 최악의 상황까지 탐색하는데 보통 이 부분에서 이분 탐색을 이용해 시간 복잡도를 log 로 만들어야 함.

    시간에 대해 이분 탐색을 실시하면 mid 값에 해당하는 총 소요시간을 구한다.
    각 도시의 트럭마다 왕복할 수 있는 횟수를 총 소요시간을 이용해 구한다.
    각 도시마다 총 소요시간 동안 옮길 수 있는 금과 은, 금+은의 양 모두 더하고 이 값들이 기준을 충족하면 탐색 범위를 조절한다.

* 기타
    최적화 -> 결정 문제 변환 문제는 처음보면 거의 못 품.
    여러 번 보더라도 보통 반복문을 많이 돌아야 하므로 이분 탐색을 사용하지 않으면 효율성에서 나가리 됨.
    이런 유형 문제들 연습을 더 많이 해야할 듯?

'''

def solution(a, b, g, s, w, t):
    start, end = 0, (10 ** 9) * (10 ** 5) * 4
    answer = end

    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0

        for i in range(len(g)):
            # 현재 도시의 정보
            now_gold = g[i]
            now_silver = s[i]
            now_weight = w[i]
            now_time = t[i]

            # 주어진 시간내에서 이동할 수 있는 횟수(왕복으로 계산)
            move_cnt = mid // (now_time * 2)

            # 편도 추가
            if mid % (now_time * 2) >= now_time:
                move_cnt += 1

            # 직선의 벡터 방정식으로 증명.
            gold += now_gold if (now_gold < move_cnt * now_weight) else move_cnt * now_weight
            silver += now_silver if (now_silver < move_cnt * now_weight) else move_cnt * now_weight
            total += now_gold + now_silver if (now_gold + now_silver < move_cnt * now_weight) else move_cnt * now_weight

        print(mid, move_cnt, gold, silver, total)
        if gold >= a and silver >= b and total >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    return answer