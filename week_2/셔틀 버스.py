'''
* 유형
    구현

* 체감 난이도
    **+

* 풀이
    1. 주어진 버스 시간표와 크루들의 도착 시간을 이용해 각 버스에 크루들을 다 태워본다.
    2. 막차에 탄 크루들의 도착시간을 보며 콘이 언제 도착하게 할 지 결정한다.
        막차가 꽉 차지 않았다면 막차 시간 맞춰서 도착하면 됨.
        막차가 꽉 찼다면, 막차에 탄 크루 중 마지막에 도착한 크루보다 1 분 먼저 도착하게 한다.

    막차를 타지 못하는 크루들은 배제한다.

'''

def solution(n, t, m, timetable):
    busPlan = {i * t: [] for i in range(n)}  # {offset: maxCrew}, offset 은 분단위
    timetable = sorted(timetable)

    # 버스에 크루들을 태우기
    for i, offset in enumerate(busPlan):
        while len(timetable) > 0:
            test = timetable[0]
            hour, minute = test[:2], test[3:]
            crewOffset = (int(hour) - 9) * 60 + int(minute)
            if len(timetable) > 0 and crewOffset <= offset:
                pop = timetable.pop(0)
                busPlan[offset].append(pop)
                if len(busPlan[offset]) >= m:
                    break
            else:
                break

    # 막차부터 젤 늦게 탈 곳 탐색
    # 막차에 꽉 안 찼으면 시간 맞춰서 타기
    # 꽉 찼으면 젤 마지막 사람보다 1 분 빨리 타기
    last = list(busPlan.keys())[-1]
    lastCrews = busPlan[last]
    if len(lastCrews) >= m:
        # 한 놈 내리기
        lc = lastCrews[-1]
        lcOffset = (int(lc[:2]) - 9) * 60 + int(lc[3:])
        conOffset = lcOffset - 1

    else:
        # 버스 시간 맞춰서 타기
        time = last
        conOffset = time

    conOffset = conOffset + 540
    div, mod = divmod(conOffset, 60)
    hour = str(div) if div >= 10 else '0' + str(div)
    minute = str(mod) if mod >= 10 else '0' + str(mod)
    return f'{hour}:{minute}'


# --------------------------------------------

# short version
def solution(n, t, m, timetable):
    busPlan = {i * t: [] for i in range(n)}
    timetable = sorted(timetable)
    for i, offset in enumerate(busPlan):
        while len(timetable) > 0:
            crewOffset = (int(timetable[0][:2]) - 9) * 60 + int(timetable[0][3:])
            if len(timetable) > 0 and crewOffset <= offset:
                busPlan[offset].append(timetable.pop(0))
                if len(busPlan[offset]) >= m:
                    break
            else:
                break
    lastCrews = busPlan[list(busPlan.keys())[-1]]
    conOffset = 540 + (int(lastCrews[-1][:2]) - 9) * 60 + int(lastCrews[-1][3:]) - 1 if len(lastCrews) >= m else 540 + list(busPlan.keys())[-1]
    div, mod = divmod(conOffset, 60)
    return f'{str(div) if div >= 10 else "0" + str(div)}:{str(mod) if mod >= 10 else "0" + str(mod)}'