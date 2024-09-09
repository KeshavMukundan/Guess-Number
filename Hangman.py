from random import choice
from time import sleep
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
words_split = ["_" * len(word) for word in words]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

count = 0

def check_index(guess, word):
    indices = []
    for i, element in enumerate(word):
        if element == guess:
            indices.append(i)
    return indices
    


def check_letter(guess, word, wordspace):
    global count 
    
    if guess in word:
        index = check_index(guess, word)
        for i in index:
            wordspace[i] = guess
        print(*wordspace)
    else:
        count += 1
        hangman()
        if count == 6:
            print("Sorry! You lose!")
            
            return
        
        
def hangman():

    match (count):
        case 0:
            print(HANGMANPICS[0])
        case 1:
            print(HANGMANPICS[1])
        case 2:
            print(HANGMANPICS[2])
        case 3:
            print(HANGMANPICS[3])
        case 4:
            print(HANGMANPICS[4])
        case 5:
            print(HANGMANPICS[5])
        case 6:
            print(HANGMANPICS[6])
            

def game():
    word = choice(words)
    wordspace = ["_" for _ in range(len(word))]
    print(*wordspace)

    while True:
        if "_" not in wordspace or count == 6:
            break
        else:
        
            guess = input("Enter a guess(letter): ").lower()
            
            if len(guess) == 1:
                check_letter(guess, word, wordspace)
                
            else:
                print("Please enter a letter")



def main():
    print("Welcome to Hangman Game")
    sleep(2)
    print("************************")
    print("press any key to play (1 to exit)")
    print("************************")
    sleep(2)
    ask = input()
    if ask != "1":
        game()
    else:
        print("BYE!!")
    

if __name__ == "__main__":
    main()