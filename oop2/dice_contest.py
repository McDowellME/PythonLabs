#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Running a simulation with our classes"""

# lab 70 https://live.alta3.com/content/tlg-sde-python/labs/content/pyb/LAB_object-oriented-programming_oop_classes_03.html

# import our classes
from cheatdice import *

def main():
    """called at runtime"""

    # the player known as the swapper
    swapper = Cheat_Swapper()
    # the player known as the loaded_dice
    loaded_dice = Cheat_Loaded_Dice()
    # the player knows as the mulligan
    mulligan = Cheat_Mulligan()

    # track scores for both players
    player1_score = 0
    player2_score = 0

    # how many games we want to run
    number_of_games = 100000
    game_number = 0

    # begin!
    print("Simulation running")
    print("==================")
    while game_number < number_of_games:
        # choose players
        player1 = swapper
        player2 = mulligan

        player1.roll()
        player2.roll()

        # swapper.roll()
        # loaded_dice.roll()
        # mulligan.roll()

        player1.cheat()
        player2.cheat()
        
        # swapper.cheat()
        # loaded_dice.cheat()
        # mulligan.cheat()        

        """Remove # before print statements to see simulation running
           Simulation takes approximately one hour to run with print
           statements or ten seconds with print statements
           commented out"""      

        #print("Cheater 1 rolled" + str(swapper.get_dice()))
        #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
        if sum(player1.get_dice()) == sum(player2.get_dice()):
            #print("Draw!")
            pass
        elif sum(player1.get_dice()) > sum(player2.get_dice()):
            #print(f"{player1} wins!")
            player1_score += 1
        else:
            #print(f"{player2} wins!")
            player2_score += 1
        game_number += 1

    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(type(player1).__name__ + f" won: {player1_score}")
    print(type(player2).__name__ + f" won: {player2_score}")

    # determine the winner
    if player1_score == player2_score:
        print("Game was drawn")
    elif player1_score > player2_score:
        print(type(player1).__name__ + " won most games")
    else:
        print(type(player2).__name__ + " won most games")

if __name__ == "__main__":
    main()