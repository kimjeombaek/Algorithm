def solution(sizes: list) -> int:
    w, h = 0, 0
    for size in sizes:
        uw, uh = max(size), min(size)
        if uw > w:
            w = uw
        if uh > h:
            h = uh
    answer = w * h
    return answer