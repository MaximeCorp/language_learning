import sys

import vocab
import training
import variables

main_name = "Main menu"
main_options = ["Training", "Vocabulary", "Stats"]

training_name = "Training menu"
training_options = ["Symbols", "Words", "Sentences", "Go back to main menu"]

vocab_name = "Vocabulary menu"
vocab_options = ["Add vocabulary", "Search word", "Show dictionnary", "Go back to main menu"]

stats_name = "Stats menu"
stats_options = ["Stats per word", "Overall stats", "Go back to main menu"]

names = [main_name, training_name, vocab_name, stats_name]
options = [main_options, training_options, vocab_options, stats_options]

def get_int(message):
    result = input(message)
    while len(result) == 0 or not (result.isdigit() or (result[0] == '-' and result[1:].isdigit)):
        print()
        result = input(f"{variables.RED}A number was expected...{variables.RESET}\n")

    return int(result)

def main_loop(name, options):
    print(f"{variables.GREEN}{name}:")
    for i in range(len(options)):
        print(f"  {variables.BLUE}{i}.{variables.RESET} {options[i]}")
    print()

    choice = get_int("")

    while choice < -1 or choice > len(options) - 1:
        choice = get_int(f"{variables.RED}Value should be within 0 and {len(options) - 1}...{variables.RESET}\n")

    print()

    return choice

def choice_parser(cur, choice):
    if choice == -2:
        choice = main_loop(names[cur], options[cur])
    elif cur == 0:
        if choice == 0:
            choice = main_loop(training_name, training_options)
            cur = 1
        elif choice == 1:
            choice = main_loop(vocab_name, vocab_options)
            cur = 2
        elif choice == 2:
            choice = main_loop(stats_name, stats_options)
            cur = 3
        else:
            choice = -1
    elif cur == 1:
        if choice == 0:
            training.shuffle_letters()
            choice = -2
        elif choice == 1:
            training.shuffle_words()
            choice = -2
        elif choice == 2:
            training.phrase_exercise()
            choice = -2
        elif choice == 3:
            choice = main_loop(main_name, main_options)
            cur = 0
    elif cur == 2:
        if choice == 0:
            vocab.add_vocab()
            choice = -2
        elif choice == 1:
            vocab.voc_search()
            choice = -2
        elif choice == 2:
            vocab.print_dict()
            choice = -2
        elif choice == 3:
            choice = main_loop(main_name, main_options)
            cur = 0
    elif cur == 3:
        if choice == 0:
            choice = -2
        elif choice == 1:
            choice = -2
            choice = -2
        elif choice == 2:
            choice = main_loop(main_name, main_options)
            cur = 0
    else:
        choice = -1

    return choice, cur

if __name__ == "__main__":
    print(f"\n\n{variables.YELLOW}Language training script:{variables.RESET}\n")
    choice = main_loop(main_name, main_options)

    cur = 0

    while choice != -1:
        choice, cur = choice_parser(cur, choice)
