from display import display_intro, display_round_number, display_player_card, display_round_result, display_end_of_game

def play_game(deck):
#Intro
    display_intro()

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
    for round_num in range(1, 11):                                          #10 round game length
        display_round_number(round_num)                                     #Print round number
        player_card = deck.draw()                                           #Draw player's card
        cpu_card = deck.draw()                                              #Draw cpu's card

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
