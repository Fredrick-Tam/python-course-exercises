import random
def declare(t):
    r = random.random()
    if r > t:
        return 2
    else:
        return 1
def p2_win(num_1, num_2):
#this will tell me if, based on the numbers that each player declares, whether
#player 2 won/lost
    if (num_1+num_2)%2 == 0:
        return True
    else:
        return False

def main():
    p1_money = 0
    p2_money = 0
    mode = raw_input ('If you want to play Player vs. Computer, type "1". If you want to play Computer vs. Computer, type "2":')
    if mode == "1":
        threshold_1 = 0.6
        while True:
            computer_answer = declare(threshold_1)
            user_answer = raw_input ("Type the number 1 or 2:")
            user_answer = int(user_answer)
            if p2_win(user_answer, computer_answer):
                p2_money = p2_money + (user_answer+computer_answer)
                p1_money = p1_money - (user_answer+computer_answer)
                print "Computer wins! It has %f dollars" % (p2_money)
            else:
                p1_money = p1_money + (user_answer+computer_answer)
                p2_money = p2_money - (user_answer+computer_answer)
                print "You win! You have %f dollars" % (p1_money)
            play_again = raw_input ("Do you want to play again? Type yes or no:")
            if play_again == "no":
                break
    else:
        threshold_1 = 0.7
        threshold_2 = 0.4
        while True: 
            computer1_answer = declare(threshold_1)
            computer2_answer = declare(threshold_2)
            if p2_win(computer1_answer, computer2_answer):
                p2_money = p2_money + (computer1_answer+computer2_answer)
                p1_money = p1_money - (computer1_answer + computer2_answer)
                print "Computer 2 wins! It has %f dollars" % (p2_money)
            else:
                p1_money = p1_money + (computer1_answer+computer2_answer)
                p2_money = p2_money - (computer1_answer+computer2_answer)
                print "Computer 1 wins! It has %f dollars" % (p1_money)
            play_again = raw_input ("Do you want to play again? Type yes or no:")
            if play_again == "no":
                break
main()
