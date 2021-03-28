# Rock Paper Scissor
import random, math
def Game():
    print("Welcome to Rock-Paper-Scissor Game!")
    print("1: Rock, 2: Paper, 3: Scissor")
    choice = input("Enter your choice:")
    dic = {1: 'Rock', 2: 'Paper', 3: 'Scissor'}
    random_choice = random.randrange(0,4)
    if (choice == random_choice):
        print("Tie, Both have  ",dic([choice]))
    else:
        if choice == 1 and random_choice == 2:
            print("You Lost, Paper beats Rock")
        elif choice == 1 and random_choice == 3:
            print("You Won, Rock beats Sicssor")
        elif choice == 2 and random_choice == 1:
            print("You Won, Paper beats Rock")
        elif choice==2 and random_choice==3:
            print("You Lost, Sicssor beats Paper")
        elif choice==3 and random_choice==1:
            print("You Lost, Rock beats Scissor")
        elif choice==3 and random_choice==2:
            print("You Won, Scissor beats Rock")
        else:
            print("Please enter a number between 1-3")
            Game()
    
    q = input("Do you ant to play again? (y/n)")
    if q == 'y' or q == 'Y':
        Game()
    else:
        print("Thanks for playing :)")    

Game()