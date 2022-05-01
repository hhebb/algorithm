'''
* 유형
    구간합, DP

* 체감 난이도
    ****

'''


def str2int(time):
    h, m, s = time.split(':')
    total = 3600 * int(h) + 60 * int(m) + int(s)
    return total


def int2str(time):
    h, remain = divmod(time, 3600)
    m, s = divmod(remain, 60)
    h = str(h) if len(str(h)) == 2 else '0' + str(h)
    m = str(m) if len(str(m)) == 2 else '0' + str(m)
    s = str(s) if len(str(s)) == 2 else '0' + str(s)
    return ':'.join([h, m, s])


def solution(play_time, adv_time, logs):
    answer = ''
    play_time = str2int(play_time)
    adv_time = str2int(adv_time)
    bucket = [0] * (play_time + 1)

    for log in logs:
        start, end = log.split('-')
        start = str2int(start)
        end = str2int(end)
        bucket[start] += 1
        bucket[end] -= 1

    for t in range(1, len(bucket)):
        bucket[t] += bucket[t - 1]

    for t in range(1, len(bucket)):
        bucket[t] += bucket[t - 1]

    most_view = 0
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < bucket[i] - bucket[i - adv_time]:
                most_view = bucket[i] - bucket[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < bucket[i]:
                most_view = bucket[i]
                max_time = i - adv_time + 1
    answer = int2str(max_time)
    return answer