from random import randint
from collections import OrderedDict
myListOfWords = ['sonofsatyamurthy', 'avengers', 'prefontaine', 'pandeyji',
                 'happydon', 'rohanbasha', 'satnamwaheguru', 'eelueelu', 'canada', 'honalulu', 'California', 'balleballe', 'terminator']
play = True

while(play):
    guess = []
    correctGuess = []
    print("-------HANGMAN----------")
    print("1. Play Hangman.")
    print("2. Quit")
    print("Entre ton choix:", end="")
    choice = int(input())
    if (choice == 1):
        randomQuiz = randint(0, len(myListOfWords)-1)
        wordOfGame = myListOfWords[randomQuiz]
        xtra = list(OrderedDict.fromkeys(wordOfGame))
        i = 0
        nbTries = int((len(wordOfGame)+2)/2)
        print(nbTries)
        print("Remember you only got "+str(nbTries)+" tries..")
        print("Your Quiz is :")
        for x in range(0, len(wordOfGame)):
            print("_ ", end="")
        while(i < nbTries):
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
                    print("\n\n- =\--------WINNER---------/= -\n\n")
                    break
                print("\nCooool now the next one..")
            else:
                i = i+1
                print("Progress")
                for y in wordOfGame:
                    if (y in correctGuess):
                        print(y, end=" ")
                    else:
                        print("_", end=" ")
                print("\n\nSorry "+guessletter+" is not present in the word.")
                print(str(nbTries-i) + " lives left.")

        if(i == nbTries):
            print("\n\n--\You lost the game/--\n\n")

    if (choice == 2):
        print("Merci de jouer au jeu")
        play = False
