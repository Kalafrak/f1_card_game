import random
from deck import Deck
from driver_class import load_drivers

def play_game(deck):
#Intro
    user_ready = input("Are you ready to race!! (y/n)")
    if user_ready.lower() in ["y", "yes"]:
        print("It's cards out and away we go!!")
    else:
        print("Bye then, Rookie!")
        return

#Main game loop
    for round_num in range(1, 11):                  #10 round game length
        print(f"{'=' * 21}\n{'Round ' + str(round_num):^21}\n{'=' * 21}")
        player_card = deck.draw()                   #Draw player's card
        cpu_card = deck.draw()                      #Draw cpu's card


