#BOJ1725:히스토그램
import sys

def hist(s, e):
    if s == e:
        return 0
    if s+1 == e:
        return A[s]
    
    mid = (s+e) // 2
    answer = max(hist(s, mid), hist(mid, e))
    
    w = 1
    h = A[mid]
    l, r = mid, mid
    p, q = 0, 0
    while (r-l+1) < (e-s): # 3-3+1 < 6
        
        if l > s:
            p = min(h, A[l-1])
        else: p = -1
        
        if r < e-1:
            q = min(h, A[r+1])
        else: q = -1
        
        # 높이 결정
        if p > q:
            h = p
            l -= 1
        else:
            h = q
            r += 1
        
        w+=1
        answer = max(answer, w*h)
    return answer

N = int(input())
A = []

for _ in range(N):
    val = int(sys.stdin.readline())
    A.append(val)
    
print(hist(0, N))