n = int(input())
nqs = input().replace(' ', '')

arr = []

def recur(used, remain):
    if len(used) == n+1:
        arr.append(used)
        return

    for i, rem in enumerate(remain):
        if len(used) > 0:
            if (nqs[len(used)-1] == '<' and used[-1] < rem) or (nqs[len(used)-1] == '>' and used[-1] > rem):
                rem_copy = list(remain).copy()
                rem_copy.pop(i)
                recur(used + [rem], rem_copy)
        else:
            rem_copy = list(remain).copy()
            rem_copy.pop(i)
            recur(used + [rem], rem_copy)

recur([], range(10))

print(len(arr))
print(''.join([str(a) for a in arr[-1]]))
print(''.join([str(a) for a in arr[0]]))