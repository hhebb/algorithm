'''
* 유형
    연결 리스트, 구현

* 체감 난이도
    ***

* 풀이
    1. 처음에 리스트로 단순하게 풀었는데 당연히 효율성 테스트에서 막힘.
        O(N) 이 걸리는 insert, pop 하는 과정이 포함되다보니 오래 걸림.
    2. 리스트를 딕셔너리로 바꿔서 풀려고 했지만 로직 구성을 못했음.
    3. 스택과 이중 연결 리스트 이용해서 풀려고 했지만 로직 구성에 실패.

    해답은 이중 연결 리스트로 푸는 것이 맞는데
    중요한 건
        1. 스택에 삭제한 행을 push 할 때 노드 통째로 넣어줘야함.
        2. 링크드 리스트의 노드를 실제로 삭제하지 않아야 함.
        3. 현재 선택된 행을 정확하게 지정해야 함.

    노드의 링크 조작만 제대로 할 수 있으면 풀 수 있음.
    그리고 스택이기 때문에 되돌리기는 순서대로 수행되어 링크가 꼬일 일은 발생하지 않는다!!


'''


def solution(n, k, cmd):
    table = {i: [i - 1, i + 1] for i in range(1, n + 1)}
    current = k + 1
    stack = []
    result = ['O'] * n

    for c in cmd:
        if c[0] == 'D' or c[0] == 'U':
            direc = 1 if c[0] == 'D' else 0
            dist = int(c[2:])
            for i in range(dist):
                current = table[current][direc]
        elif c[0] == 'C':
            result[current - 1] = 'X'
            front, back = table[current]
            stack.append((front, back, current))
            current = table[current][0] if back == n + 1 else table[current][1]

            if front == 0:
                table[current][0] = front
            elif back == n + 1:
                table[current][1] = back
            else:
                table[front][1] = back
                table[back][0] = front

        elif c[0] == 'Z':
            front, back, saved = stack.pop()
            result[saved - 1] = 'O'
            if front == 0:
                table[back][0] = saved
            elif back == n + 1:
                table[front][1] = saved
            else:
                table[front][1] = saved
                table[back][0] = saved

    return ''.join(result)