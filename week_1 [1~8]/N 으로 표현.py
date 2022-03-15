'''
* 문제 유형
    DP

* 체감 난이도
    ***+

* 풀이
    N 을 하나씩 추가하며 나올 수 있는 경우를 모두 검사한다.
    N 에 대해서 메모이제이션을 수행한다.

    N 을 1 개 사용하는 경우
    N 을 2 개 사용하는 경우 = N 을 1 개 사용하는 경우, N 을 1 개 사용하는 경우의 모든 조합
    N 을 3 개 사용하는 경우 = (N 을 2 개 사용하는 경우, N 을 1 개 사용하는 경우) + (N 을 1 개 사용하는 경우, N 을 2 개 사용하는 경우)
    N 을 4 개 사용하는 경우 = (N_1, N_3) + (N_2, N_2) + (N_3, N_1)
    ...

    이 처럼 N 마다 모든 나올 수 있는 경우를 저장하여 다음 N 일 때 사용한다.

    원하는 수 number 가 나오면 바로 리턴한다.


* 기타
    1. 재귀나 permutation 을 이용해 모든 경우를 뽑으려고 하니 괄호를 처리하기가 너무 까다로웠음.
        level 2 문제 중에 비슷한 문제가 있는데 이 문제는 DP 로 푸는게 훨씬 간편해 보임.

* 결과
    테스트 1 〉	통과 (1.11ms, 10.5MB)
    테스트 2 〉	통과 (0.03ms, 10.4MB)
    테스트 3 〉	통과 (0.03ms, 10.3MB)
    테스트 4 〉	통과 (22.48ms, 11.3MB)
    테스트 5 〉	통과 (16.66ms, 11.2MB)
    테스트 6 〉	통과 (0.24ms, 10.4MB)
    테스트 7 〉	통과 (0.26ms, 10.4MB)
    테스트 8 〉	통과 (22.63ms, 11.2MB)
    테스트 9 〉	통과 (0.02ms, 10.4MB)

'''

def solution(N, number):
    dp = {i: set() for i in range(10)} # 각각 N 을 k 개 사용했을 때 나오는 총 경우
    dp[0] = set([0])
    dp[1] = set([N])
    for i in range(1, 9):
        # N 이 연속으로 붙은 경우 하나 추가.
        dp[i+1].add(int(str(N)*(i+1)))

        # ex) i 가 5 일 때
        #       j = 1, 2, 3, 4
        #       k = 4, 3, 2, 1 (k=i-j)
        for j in range(1, i):
            for l in dp[j]:
                for m in dp[i-j]:
                    # 이 코드는 나눗셈 제외한 연산 결과를 한 번에 추가하는데, 시간이 너무 오래걸려버림.
                    # dp[i] = dp[i].union([l+m, l*m, l-m, m-l])

                    # +, * 은 순서가 바뀌어도 결과가 같으므로 한 번만 추가해 줌.
                    dp[i].add(l+m)
                    dp[i].add(l*m)

                    # -, // 은 순서가 바뀌면 결과가 바뀌므로 2 번 추가해 줌.
                    dp[i].add(l-m)
                    dp[i].add(m-l)

                    # division by zero 방지하기 위함.
                    # try except 로 감싸도 무방함.
                    dp[i].add(l//m) if m != 0 else None
                    dp[i].add(m//l) if l != 0 else None

                    # print(dp[i])
        # number 가 나타나면 바로 리턴
        if number in dp[i]:
            return i

    # number 가 나타나지 않으면 -1 반환
    return -1