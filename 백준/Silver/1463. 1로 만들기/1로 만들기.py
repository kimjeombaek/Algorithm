N = int(input())

lst = [0 for _ in range(10000001)]

for i in range(1, N + 1):
    if i == 1:
        lst[i] = 0
        continue
    lst[i] = lst[i-1] + 1
    if i % 3 == 0 and lst[i//3] + 1 < lst[i]:
        lst[i] = lst[i//3] + 1
    if i % 2 == 0 and lst[i//2] + 1< lst[i]:
        lst[i] = lst[i//2] + 1
        
print(lst[N])