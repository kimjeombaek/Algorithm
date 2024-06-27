def solution(answers: list) -> list:
    players = [[1, 2, 3, 4, 5],
               [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer_dict = {}
    
    for player_number, method in enumerate(players):
        cnt = 0
        for idx, goal in enumerate(answers):
            if goal == method[idx%len(method)]:
                cnt += 1
                answer_dict[player_number+1] = cnt
    return sorted([x[0] for x in answer_dict.items() if x[1] == max(answer_dict.values())])