import re
import numpy

card_file = 'card.txt'


def text_file_to_dict(file_path, part):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        if part == 1:
            [times, distances] = [re.sub("\s+", ",", line.strip()).split(':,')[-1].split(',') for line in lines]
            my_dict = {int(times[i]): int(distances[i]) for i in range(len(times))}
        else:
            [time, distance] = [re.sub("\s+", ",", line.strip()).split(':,')[-1].replace(',', '') for line in lines]
            my_dict = {int(time): int(distance)}
        return my_dict


def get_answer(file_path, part):
    card_dict = text_file_to_dict(file_path, part)
    ways_to_win_list = []
    for t, d in card_dict.items():
        ways_to_win_race = 0
        for hold_sec in range(0, t + 1):
            formula = (t - hold_sec) * hold_sec
            if formula > d:
                ways_to_win_race += 1
        ways_to_win_list.append(ways_to_win_race)

    return numpy.prod(ways_to_win_list)


for problem_part in [1, 2]:
    answer = get_answer(card_file, problem_part)
    print(answer)
