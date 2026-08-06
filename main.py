from deck import Deck
from driver_class import load_drivers
from game_loop import play_game
from display import display_mode_menu



#Main game loop function
def main():
    drivers = load_drivers("drivers.json")
    deck = Deck(drivers)
    deck.shuffle()
    mode = display_mode_menu()
    if mode is None:
        return
    play_game(deck, mode)

if __name__ == "__main__":
    main()