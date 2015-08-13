import player_vs_computer  
import computer_vs_computer  



def main():
### Options to choose from comp vs. comp or player vs. comp
    
    player_select = raw_input ('''If you want to play Player vs. Computer, type "1".
     If you want to play Computer vs. Computer, type "2":''')
    if player_select == "1":
        player_vs_computer.game1()
    else:
        computer_vs_computer.game2()
main()
