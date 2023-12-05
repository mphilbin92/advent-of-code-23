import re


def part_1():
    total_score = 0

    with open('day4/cards.txt', 'r') as in_file:
        for i in in_file:
            winning_nums = i.split('|')[0].split(':')[-1].strip()
            my_nums = i.split('|')[-1].strip()

            winning_nums_re = re.sub("\s+", r",", winning_nums)
            my_nums_re = re.sub("\s+", r",", my_nums)

            winning_nums_list = winning_nums_re.split(',')
            my_nums_re_list = my_nums_re.split(',')

            line_matches = set(my_nums_re_list).intersection(winning_nums_list)

            score = 0
            for num, m in enumerate(line_matches):
                if num == 0:
                    score += 1
                else:
                    score *= 2

            total_score += score

    print(total_score)
