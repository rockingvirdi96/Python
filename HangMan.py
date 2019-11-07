import random
from collections import OrderedDict
myListOfWords = ['pythonp', 'scripting', 'prefontaine']
guess = []
correctGuess = []
play = True

while(play):
    print("-------HANGMAN----------")
    print("1. Play Hangman.")
    print("2. Quit")
    choice = int(input())
    i = 0
    z = 0
    if (choice == 1):
        randomQuiz = random.randint(0, 2)
        wordOfGame = myListOfWords[randomQuiz]
        xtra = list(OrderedDict.fromkeys(wordOfGame))

        print(len(xtra))
        print("Remember you only got "+str(int(len(wordOfGame)/2))+" tries..")
        print("Your Quiz is :")
        for x in range(0, len(wordOfGame)):
            print("_ ", end="")
        while(i < int(len(wordOfGame)/2)):
            isnotchar = True
            while(isnotchar):
                print("\nEnter your guessed letter:")
                guessletter = input()
                if (len(guessletter) == 1):
                    isnotchar = False
                else:
                    print("Only single character is allowed.")
            if (guessletter in guess):
                print("You already guessed this letter.")
                continue
            guess.append(guessletter)
            if(guess[len(guess)-1] in wordOfGame):
                correctGuess.append(guessletter)
                print("Progress")
                for y in wordOfGame:
                    if (y in correctGuess):
                        print(y, end=" ")
                    else:
                        print("_", end=" ")
                if(len(correctGuess) == len(xtra)):
                    print("\nYou win the game.")
                    break
                print("\nCooool now the next one..")
            else:
                i = i+1
                print("Sorry "+guessletter+" is not present in the word.")

        if(i == int(len(wordOfGame)/2)):
            print("You lost the game")

    if (choice == 2):
        print("Merci de jouer au jeu")
        play = False
