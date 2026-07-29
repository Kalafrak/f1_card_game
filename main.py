import random
from deck import Deck
from driver_class import load_drivers
from game_loop import play_game



#Main game loop function
def main():
    drivers = load_drivers("drivers.json")
    deck = Deck(drivers)
    deck.shuffle()
    play_game(deck)

if __name__ == "__main__":
    main()