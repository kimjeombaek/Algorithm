from collections import deque

n = int(input())
lst = deque([i for i in range(1, n+1)])

while (len(lst) > 1):
    lst.popleft()
    back = lst.popleft()
    lst.append(back)
print(lst[0])