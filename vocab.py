def is_new(learning, word, meaning):
    for translation in learning:
        if translation[0] == word and translation[1] == meaning:
            return False
    return True

def add_vocab():
    with open("words", "r") as file:
        content = file.read().replace("\n", "")

    learning = content.split(',')

    print(f"Collection of {len(learning)} words\n")

    for i in range(len(learning)):
        learning[i] = learning[i].split('=')

    word = input("New word:\n")
    if word != "quit":
        meaning = input("Meaning:\n")

    while word != "quit" and meaning != "quit":
        if is_new(learning, word, meaning):
            with open('words', 'a') as file:
                file.write(f",{word}={meaning}")
            learning.append([ word, meaning ])
            with open('stats', 'a') as file:
                file.write(f",{word}=0/0")
        else:
            print(f"\"{word}\"=\"{meaning}\" already in words list")
        word = input("New word:\n")
        if word != "quit":
            meaning = input("Meaning:\n")

    print("All words added to dictionnary")


def voc_search():
    with open("words", "r") as file:
        content = file.read()

    learning = content.split(',')
    for i in range(len(learning)):
        learning[i] = learning[i].split('=')

    while True:
        word = input("Search a word:\n")

        if word == "quit":
            break

        arr1 = [x[1] for x in learning if x[0] == word]
        arr2 = [x[0] for x in learning if x[1] == word]

        print(arr1)
        print(arr2)


def print_dict():
    with open("words", "r") as file:
        content = file.read()
    learning = content.split(',')
    for i in range(len(learning)):
        learning[i] = learning[i].split('=')
    print(f"{len(learning)} words:")
    for word in learning:
        print(f"    {word[0]} = {word[1]}")
