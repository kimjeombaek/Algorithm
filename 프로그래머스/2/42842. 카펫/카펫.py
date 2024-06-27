def solution(brown: int, yellow: int) -> list:
    """ 갈색 타일과 노란 타일의 개수를 사용해서 카펫의 가로와 세로 크기를 찾는 함수

    Args:
        brown (int): 갈색 타일 수 (8 <= brown <= 5k)
        yellow (int): 노란색 타일 수 (1 <= yellow <= 20k)

    Returns:
        list: 카펫의 가로(row), 세로(col) 크기를 리스트로 반환 (col <= row)
    """
    answer = []
    total = brown + yellow
    for row in range(3, total // 3 + 1):
        if total % row == 0:
            col = total // row
            if (row - 2) * (col - 2) == yellow:
                answer = [row, col]
    return answer