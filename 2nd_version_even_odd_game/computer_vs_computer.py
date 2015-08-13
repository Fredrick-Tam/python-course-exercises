import random
def game2():
    number_1 = random.random()
    t1 = random.random()
    if number_1 < t1:
        x = 1
    if number_1 > t1:
        x = 2
    
    number_2 = random.random()
    t2 = random.random()
    if number_2 < t2:
        y = 1
    if number_2 > t2:
        y = 2
    
    computer1_money = 0
    computer2_money = 0

    computer1_move = x 
    computer2_move = y

    total = computer1_move + computer2_move
        
    if total % 2 !=  0:
        computer1_money = computer1_money + total 
        computer2_money = computer2_money - total   
        print "Player 1 won " + str(total) + " dollar(s)"
        print "Player 1 now has " + str(computer1_money) + " dollar(s)"     
        print "Player 2 lost " + str(total) + " dollar(s)"
        print "Player 2 now has " + str(computer2_money) + " dollar(s)"
        
    if total % 2 ==  0:
        computer1_money = computer1_money - total 
        computer2_money = computer2_money + total
        print "Player 1 lost " + str(total) + " dollar(s)"   
        print "Player 1 now has " + str(computer1_money) + " dollar(s)"     
        print "Player 2 won " + str(total) + " dollar(s)"
        print "Player 2 now has " + str(computer2_money) + " dollar(s)"