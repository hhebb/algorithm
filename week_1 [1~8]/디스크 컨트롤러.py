'''

* 유형
    heap

* 체감 난이도
    ***+

* 풀이
    총 시간이 가장 적게 소요되기 위해선 작은 소요시간 순서대로 처리를 해야한다.
    단, 처리 요청이 들어오는 시각은 따로 고려해야 한다.

    정리하면,
    1. 처리 요청이 접수된 작업을 heap 에 추가하는 작업
    2. heap 에서 대기하고 있는 작업 중 가장 시간이 적게 걸리는 작업 처리하며 제거.
    으로 나눠서 풀이한다.

    필요한 변수
    현재 시각, 마지막에 처리가 끝난 시각

    주의할 점은,
    heap 에서 대기하고 있는 작업이 없을 때도 있다는 점.
    이 때는 현재 시각을 1 늘려주면서 진행.
    heap 에서 대기중인 작업이 있으면 pop 하고 현재 시각을 그 작업 소요시간만큼 점프 시킨다.

*

'''

from heapq import heappush, heappop
def solution(jobs):
    h = []
    last, t = -1, 0  # 마지막 작업 종료 시점, 현재 시각
    cnt = 0
    history = []

    while len(jobs) > cnt:
        for start, duration in jobs:
            if last < start <= t:
                heappush(h, [duration, start])

        if len(h) > 0:
            dur, s = heappop(h)
            last = t
            t += dur
            cnt += 1
            history.append((t - s))
        else:
            t += 1
    # print(history)
    return sum(history) // len(history)