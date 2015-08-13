### Question 3

import random


print("Welcome to the even odd game")

again = 1
while again< 2:
    print("let us begin")

playerMove = input('enter a number, either 1 or 2')

    ### setting threshold value for computer 1
computer1Move = (random.random()*1)
threshold = 0.6
        if computer1Move >= threshold:
            computer1Move == 2
        else:
            computer1Move == 1
### How to find out who wins between player and computer 1
        if computer1Move + playerMove == 3:
            print("computer chooses %s !") % computer1Move
            print (' player1 wins and gets $3')
    
        elif computer1Move + playerMove == 2:
            print("computer chooses %s !") % computer1Move
            print (' computer wins and gets $2 ')
      
        elif computer1Move + playerMove == 4:
            print("computer chooses %s !") % computer1Move
            print (' computer wins and gets $4 ')
    again = input("wanna play again? ( 1 for yes, 2 for no): ")
    # print goodbye
print( "Thanks for playing the even-odd game")
