import random
def main():

    print('main')

    words = []

    file1 = read_text()

    for lines in file1:
        lines = lines.replace("\n", "")
        words.append(lines)

    secretWord = random_choice(words)

    print('secret word is ', secretWord)

    secretWord = list(secretWord)# converting the chosen word a list
    guessWord = ['', '', '', '', '', '']
    errors = 0
    hangPic = hangermanGraf(errors)#Calling the graphic function

    while Game_on(errors, guessWord, secretWord):
        guess = user_input()
        if win(secretWord, guess, guessWord):
            print("correct")
        #Adding 1 to the error when the user guess wrong
        elif  secretWord.count(guess) == 0:
            errors += 1
            hangPic = hangermanGraf(errors)

    # Dealing with winning
    if secretWord == guessWord:
        print("The guess word is", ''.join(guessWord))
        print("This is the correct word.")
        print('YOU WIN!!')
        winPic = WinGUI()

    # losing
    elif errors ==6:
        print("You have" , errors , "errors")
        print("you did not make it, the correct word is ", ''.join(secretWord))

#Game over GUI
def hangermanGraf(errors):
    if errors== 0:
        print ("________      ")
        print ("|      |      ")
        print ("|             ")
        print ("|             ")
        print ("|             ")
        print ("|             ")
    elif errors == 1:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|             ")
        print ("|             ")
        print ("|             ")
    elif errors == 2:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /       ")
        print ("|             ")
        print ("|             ")
    elif errors == 3:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|      ")
        print ("|             ")
        print ("|             ")
    elif errors == 4:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|\     ")
        print ("|             ")
        print ("|             ")
    elif errors == 5:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|\     ")
        print ("|     /       ")
        print ("|             ")
    else:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|\     ")
        print ("|     / \     ")
        print ("|             ")
        print ("GAME OVER!")

#Winning GUI
def WinGUI():
    print ("              ")
    print ("________      ")
    print ("|             ")
    print ("|             ")
    print ("| \ 0 /       ")
    print ("|  \|/        ")
    print ("|   |         ")
    print ("|  / \        ")
    print (" Your sentence of death has been forgiven by the KING")
    print (" You are a free man now, Enjoy your life")
    print (" You have won")

def read_text():
    try:
        file = open("word.txt", "rt")
        lines = file.readlines()
        file.close()
        return lines
    except IOError as e:# handling reading error checking if the files is found
        print("There is no such a  file name found")
        print(e)

def random_choice(words):
    secretWord = random.choice(words)#choosing a word from the file
    return secretWord

def user_input():
    guess = input("Guess a character: ")#Getting user inputs
    return guess

def Game_on( errors, guessWord, secretWord):
    if errors < 6 and guessWord != secretWord:
        print(errors, guessWord, secretWord, 'game on')
        return True
    else:
        print(errors, guessWord, secretWord, 'game over')
        return False

def win(secretWord, guess, guessWord):
    for letters in secretWord:
        if guess == letters:
            index = 0
            while index < len (secretWord):
            # changing the user guess if correct to it appropriate index
                if secretWord[index] == guess:
                    guessWord[index] = secretWord[index]
                    return guessWord[index] == secretWord[index]
                index += 1

if __name__ == '__main__':

    main()
