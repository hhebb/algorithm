'''
* 유형
    해쉬

* 체감 난이도
    ***

* 풀이
    장르 별로 음악을 분류하고 정렬하는 문제.

    1. 장르 별로 총 재생시간이 긴 순서대로 장르를 정렬한다.
    2. 각 장르에 포함된 곡들을 재생시간 순으로 정렬하여 가장 재생시간이 긴 2 개 (최대 2개 ) 의 곡을 answer 에 추가한다.

    - python 정렬은 안정정렬이므로 순서가 뒤바뀌지 않음을 이용



'''

from collections import defaultdict

def solution(genres, plays):
    answer = []
    total_play = defaultdict(int)
    infos = defaultdict(dict)

    for i, (g, p) in enumerate(zip(genres, plays)):
        total_play[g] += p
        infos[g][i] = p

    total_play = dict(sorted(total_play.items(), key=lambda x: x[1], reverse=True)).keys()

    for genre in total_play:
        info = sorted(infos[genre].items(), key=lambda x: (x[1]), reverse=True)
        answer.extend([tmp[0] for tmp in info[:2]])
    return answer