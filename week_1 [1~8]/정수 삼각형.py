'''
* 유형
    DP

* 체감 난이도
    **

* 풀이
    전형적인 DP 문제

    점화식
    table[i][j] = max(table[i-1][j-1] + triangle[i][j], table[i-1][j] + triangle[i][j])
        table[i][j] = table[i-1][j] + triangle[i][j] (where j == 0)
        table[i][j] = table[i-1][j-1] + triangle[i][j] (where j == i-1)

    이 식을 따라서 table 을 채워나간 후 마지막 줄에서 최대값을 찾으면 답이 된다.

'''


def solution(triangle):
    table = [[0] * len(tri) for tri in triangle]
    table[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                table[i][j] = table[i - 1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                table[i][j] = table[i - 1][j - 1] + triangle[i][j]
            else:
                table[i][j] = max(table[i - 1][j - 1] + triangle[i][j], table[i - 1][j] + triangle[i][j])
    # print(table)
    return max(table[-1])