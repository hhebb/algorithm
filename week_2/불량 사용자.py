'''
* 유형
    백트랙, 구현

* 난이도
    **+

* 풀이
    1. 자료 구성
        각 제재 아이디 당 해당이 될 수 있는 유저 아이디들을 리스트로 저장한다. (candid)
    2. 경우의 수 탐색
        제재 아이디에 유저 아이디 하나씩 매칭시키며 매칭 결과를 저장한다.
        유저 아이디 매칭은 백트랙킹으로 구현한다. (탐색 후 값 복원)
    3. 매칭 결과 카운팅
        매칭 결과가 중복이 되는 경우도 있으므로 set 자료 구조를 이용해 중복을 제거하여
        최종 매칭 갯수를 구한다.


* 주의
    파이썬 리스트는 참조형 이므로 copy 함수를 사용해 값을 복사해야 함.
    제재 아이디 자체가 동일한 경우도 있으므로 식별해줘야 함.

'''

def solution(user_id, banned_id):
    candid = {(i, ban): [] for i, ban in enumerate(banned_id)}

    for i, ban in enumerate(banned_id):
        for user in user_id:
            if len(ban) == len(user):
                for b in range(len(ban)):
                    if not (ban[b] == user[b] or ban[b] == '*'):
                        break
                else:
                    candid[(i, ban)].append(user)

    candid = {k[0]: v for k, v in candid.items()}
    user_copy = user_id.copy()
    cases = []

    def recur(n, users):
        if n == len(banned_id):
            cases.append(users.copy())
            return

        for _id in candid[n]:
            if _id in user_copy:
                user_copy.remove(_id)
                users.append(_id)
                recur(n + 1, users)
                user_copy.append(users.pop())

    recur(0, [])
    cases = tuple(tuple(sorted(case)) for case in cases)
    return len(set(cases))