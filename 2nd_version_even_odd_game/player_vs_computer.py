import random
def game1():
    number = random.random()
    t = random.random()
    if number < t:
        choice = 1
    if number > t:
        choice = 2

    
    player_money = 0
    computer_money = 0

    restart = "yes"

    while restart == "yes":
        player_move = input("What number do you choose? (1 or 2) ")
        computer_move = choice
        total = player_move + computer_move
        
        if total % 2 !=  0:
            player_money = player_money + total 
            computer_money = computer_money - total   
            print "You won " + str(total) + " dollar(s)"
            print "You now have " + str(player_money) + " dollar(s)"     
            print "The Computer lost " + str(total) + " dollar(s)"
            print "The computer now has " + str(computer_money) + " dollar(s)"
     
        if total % 2 ==  0:
            player_money = player_money - total 
            computer_money = computer_money + total
            print "You lost " + str(total) + " dollar(s)"   
            print "You now have " + str(player_money) + " dollar(s)"     
            print "The Computer won " + str(total) + " dollar(s)"
            print "The computer now has " + str(computer_money) + " dollar(s)"
    
    restart = raw_input("Would you like to play again? (yes or no) ")
    
       
        