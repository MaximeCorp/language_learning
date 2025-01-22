import math
import random

import stats
import variables


def shuffle_letters():
    with open("symbols", "r") as file:
        content = file.read()

    learning = content.split(',')

    copy = learning.copy()

    res = []

    while len(copy) > 0:
        n = copy.pop(random.randint(0, len(copy) - 1))
        res.append(n)

    print(res)


def shuffle_words():
    stats_dict = stats.make_stats_dict()

    with open("words", "r") as file:
        content = file.read()

    learning = content.strip("\n").split(',')

    for i in range(len(learning)):
        learning[i] = learning[i].split('=')

    n = int(input(f"{variables.YELLOW}How many words?{variables.RESET}\n"))
    print("\n-----------------------------------\n")
    for k in range(n):
        print(f"{k + 1}/{n}")
        scores = []
        for i in range(len(learning)):
            cur = stats_dict[learning[i][0]]
            score = cur[0] * math.sqrt(cur[1]*100)
            scores.append(score)
        i = 0
        minimums = [i]

        for x in range(len(scores) - 1):
            if scores[i] > scores[x + 1]:
                i = x + 1
                minimums.clear()
                minimums.append(i)
            elif scores[i] == scores[x + 1]:
                minimums.append(x + 1)

        i = minimums[random.randint(0, len(minimums) - 1)]
        j = random.randint(0, 1)

        response = input(f"{variables.ORANGE}{learning[i][j]}:{variables.RESET}\n")
        failed = 0
        while response != learning[i][(j + 1) % 2]:
            failed += 1
            print(f"\n{variables.RED}Right answer: {learning[i][(j + 1) % 2]}{variables.RESET}\n")
            response = input(f"{variables.ORANGE}Try again, {learning[i][j]}:{variables.RESET}\n")
            print()
        if failed < 1:
            stats_dict[learning[i][0]][0] += 1
            print()
        stats_dict[learning[i][0]][1] += 1
        stats.write_stats(stats_dict)
        print(f"{variables.YELLOW}Correct!{variables.RESET}\n\n-----------------------------------\n")

    print("Challenge completed!\n")


def phrase_exercise():
    with open("words", "r") as file:
        content = file.read()

    learning = content.split(',')
    learning = content.split(',')
    for i in range(len(learning)):
        learning[i] = learning[i].split('=')[0]

    n = int(input(f"{variables.YELLOW}How many sentences?{variables.RESET}\n"))

    print("\n\n-----------------------------------")
    for k in range(n):
        print(f"{k + 1}/{n}")
        j = random.randint(3, 5)
        words = []
        for i in range(j):
            picked = learning[random.randint(0, len(learning) - 1)]
            while picked in words:
                picked = learning[random.randint(0, len(learning) - 1)]
            words.append(picked)

        print(f"{variables.YELLOW}Make a sentence using the following words:{variables.CYAN}")
        for word in words:
            print(word, end=' ')

        response = input(f"{variables.RESET}\n\n")
        valid_sentence = True
        for word in words:
            if not word in response:
                valid_sentence = False

        while not valid_sentence:
            print(f"\n{variables.ORANGE}All he following words should be contained:{variables.BLUE}")
            for word in words:
                print(word, end=' ')
            response = input(f"{variables.RESET}\n\n")
            valid_sentence = True
            for word in words:
                if not word in response:
                    valid_sentence = False
        print(f"\n{variables.CYAN}Good job!{variables.RESET}\n\n-----------------------------------")

    print("Challenge completed!\n")
