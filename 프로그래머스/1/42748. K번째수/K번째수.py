from typing import List

def solution(array: List[int], commands: List[List[int]]) -> List:
    """array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 반환하는 함수

    Args:
        array (List[int]): 정렬할 리스트
        commands (List[List[int]]): [i, j, k]를 원소로 이뤄진 이차원 리스트

    Returns:
        List: 연산을 적용 후 나온 결과 리스트
    """
    answer = []
    for i in range(len(commands)):
        answer.append(sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][-1]-1])
    return answer