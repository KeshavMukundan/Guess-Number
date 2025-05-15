from random import randint
from time import time

score = None
score_mode = ""

def welcome():
    print("\n")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have n chances to guess the correct number. [n is based on the difficulty you choose]")
    
def choice():
    print()
    print("Please select the difficulty level:")
    print("""1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)""")
    
    prompt = int(input("Enter your choice: "))
    chance = 0
    match(prompt):
        case 1:
            print("Great! You have selected the Easy difficulty level.")
            chance = 10
            mode = "Easy"
        case 2:
            print("Great! You have selected the Medium difficulty level.")
            chance = 5
            mode = "Medium"
        case 3:
            print("Great! You have selected the Hard difficulty level.")
            mode = "Hard"
            chance = 3
        case _:
            print("Invalid choice. Please choose from 1-3")
            mode = "Invalid Mode"
            

        
    return chance, mode
    
    
    
def game(): 
    
    global score
    global score_mode

    print()
    print("Let's start the game!")
    
    difficulty, mode = choice()
    computer = randint(1, 100)
    count = 1
    start_time = time()
    
    
    for _ in range(difficulty):
        
        if count == 4:
            hint = input("Hint? (y/N): ")
            if hint.lower() == "y":
                print(f"The number is between {computer - randint(1,6)} and {computer + randint(1,6)}")
            else:
                print("Invalid choice. Please enter (y/N)")
                break
            
        guess = int(input("Enter your guess: "))
        if computer < guess:
            print(f"Incorrect! The number is less than {guess}.")
        elif computer > guess:
            print(f"Incorrect The number is greater than {guess}.")
        elif computer == guess:
            print(f"Congratulations! You guessed the correct number in {count} attempts.")
            if score is None or count < score :
                score = count
                score_mode = mode
            print(f"Your high score: {score} ({score_mode})")
            end_time = time()
            elpased_time = end_time - start_time
            print()
            print(f"You took {elpased_time:.2f} seconds to guess the number")
            break
        count += 1
    score = count
    
    
   
        
    


def play():
    welcome()
    game()
    print("This game ended!")
    print()
    
    
def main():
    play()
    while True:
        ask = input("Play again? (y/N): ")
        if ask.lower() == "y":
            play()
        else:
            break
    

if __name__ == "__main__":
    main()
                     
       
        
        
