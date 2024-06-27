def solution(numbers: str) -> int:
    import itertools

    answer = []
    for i in range(1, len(numbers)+1):
        npr_list = list(itertools.permutations(numbers, i))
        for npr in npr_list:
            if isPrimeNumber(int(''.join(npr))):
                answer.append(int(''.join(npr)))
    print(set(answer))
    return len(set(answer))

def isPrimeNumber(number) -> bool:
    import math

    if number <= 1: return False
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i == 0:
            return False
    return True