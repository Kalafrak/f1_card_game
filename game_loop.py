from display import display_intro, display_round_number, display_hand, display_player_card, display_round_result, display_end_of_game

TOTAL_ROUNDS = 10
HAND_SIZE = 3

def play_game(deck, mode="classic"):
#Intro
    display_intro()
    check_deck_capacity(deck, mode)

#Main game loop
    player_score = 0
    cpu_score = 0
    stat_map = {
        "ta": "talent", "talent": "talent",
        "lo": "longevity", "longevity": "longevity",
        "ag": "aggression", "aggression": "aggression",
        "mo": "moxie", "moxie": "moxie",
        "hu": "humour", "humour": "humour",
        "sc": "scrupulousness", "scrupulousness": "scrupulousness",
    }
    for round_num in range(1, TOTAL_ROUNDS + 1):                            #10 round game length
        display_round_number(round_num)                                     #Print round number

        if mode == "draft":
            player_hand = deck.draw_hand(HAND_SIZE)                         #Draw player's hand
            cpu_hand = deck.draw_hand(HAND_SIZE)                            #Draw cpu's hand
            display_hand(player_hand)
            player_card = choose_card_from_hand(player_hand)
            if player_card is None:
                return
            cpu_card = choose_cpu_card(cpu_hand)
        else:
            player_card = deck.draw()                                       #Draw player's card
            cpu_card = deck.draw()                                          #Draw cpu's card
            display_player_card(player_card)

#While loop to make sure user inputs a valid stat.
        while True:
            player_chosen_stat = input("Choose a stat to attack with (ta/lo/ag/mo/hu/sc)")
            if player_chosen_stat.lower() in ["quit", "exit"]:
                print("See ya 'round, Rookie!")
                return
            if player_chosen_stat in stat_map:
                break
            print("That's not a valid stat, try again.")

        stat_name = stat_map[player_chosen_stat]                            #Matches user input to the stat_map to feed into getattr()
        player_value = getattr(player_card, stat_name)                      #Gets value from the loaded .json list of cards using key from stat_map.
        cpu_value = getattr(cpu_card, stat_name)
        result = compare_stat(player_value, cpu_value)
        change = calculate_score_change(result, player_value, cpu_value)
        if result == "player":
            player_score += change
        elif result == "cpu":
            cpu_score += change

        display_round_result(result, cpu_card, player_score, cpu_score)

    display_end_of_game(player_score, cpu_score)

    return

#Helper functions for logic only
def compare_stat(player_value, cpu_value):
    if player_value > cpu_value:
        return "player"
    elif player_value < cpu_value:
        return "cpu"
    else:
        return "tie"

def calculate_score_change(result, player_value, cpu_value):
    if result == "player":
        return player_value - cpu_value
    elif result == "cpu":
        return cpu_value - player_value
    else:
        return 0

def sum_stats(card):
    return card.talent + card.longevity + card.aggression + card.moxie + card.humour + card.scrupulousness

def choose_cpu_card(hand):
    return max(hand, key=sum_stats)

def choose_card_from_hand(hand):
    while True:
        choice = input(f"Choose a driver to race with (1-{len(hand)}): ")
        if choice.lower() in ["quit", "exit"]:
            print("See ya 'round, Rookie!")
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(hand):
            return hand[int(choice) - 1]
        print(f"That's not a valid choice, try a number between 1 and {len(hand)}.")

def cards_per_round(mode):
    return HAND_SIZE * 2 if mode == "draft" else 2

def check_deck_capacity(deck, mode, total_rounds=TOTAL_ROUNDS):
    needed = total_rounds * cards_per_round(mode)
    if len(deck.cards) < needed:
        raise ValueError(
            f"Not enough drivers in the deck for {mode} mode! Need at least {needed} "
            f"but only {len(deck.cards)} are loaded."
        )
    return needed
