
from random import choice



wordlist = ["shingo","james","i-phone","account","magic mouse"]

def hangman():
    word = choice(wordlist)
    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"

        print((" ".join(board)))
        while True:
            char = input(msg)
            if len(char) > 1:
                print("Enter a single letter!!")
                continue
            else:
                break

        if char in rletters:
            cind = rletters \
                .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
            e = wrong + 1
            print("\n".join(stages[: e]))

        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("You lose!! fuck you!!  The Answer is {}".format(word))

hangman()
