import time

def play_game(deck):
#Intro
    print("Welcome to Apex Legacy!")
    print("Follow the prompts and try to outscore your opponent in each round.")
    print("Type 'quit' at any time to leave the game. (Real racing drivers don't quit!)")
    user_ready = input("Are you ready to race!! (y/n)")
    if user_ready.lower() in ["y", "yes"]:
        print("It's cards out and away we go!!")
    else:
        print("See ya 'round, Rookie!")
        return

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
        print(f"{'*' * 50}\n{'Round ' + str(round_num):^50}\n{'*' * 50}")   #Print round number
        player_card = deck.draw()                                           #Draw player's card
        cpu_card = deck.draw()                                              #Draw cpu's card
        print("Your card is:")
        time.sleep(1.5)
        print(player_card)
#While loop to make sure user inputs a valid stat.
        while True:
            player_chosen_stat = input("Choose a stat to attack with (ta/lo/ag/mo/hu/sc)")
            if player_chosen_stat in ["quit", "exit"]:
                print("See ya 'round, Rookie!")
                return
            if player_chosen_stat in stat_map:
                break
            print("That's not a valid stat, try again.")

        stat_name = stat_map[player_chosen_stat]                            #Matches user input to the stat_map to feed into getattr()
        player_value = getattr(player_card, stat_name)                      #Gets value from the loaded .json list of cards using key from stat_map.
        cpu_value = getattr(cpu_card, stat_name)

        if player_value > cpu_value:
            print("You win this round!")
            player_score += player_value - cpu_value
            time.sleep(1.5)
            print("CPU had:")
            time.sleep(1.5)
            print(cpu_card)
            print(f"Player score: {player_score}    CPU score: {cpu_score}")
            input("Press Enter to continue...")
        elif player_value < cpu_value:
            print("Unlucky!")
            cpu_score += cpu_value - player_value
            time.sleep(1.5)
            print("CPU had:")
            time.sleep(1.5)
            print(cpu_card)
            print(f"Player score: {player_score}    CPU score: {cpu_score}")
            input("Press Enter to continue...")
        else:
            print("It's a photo finish!")
            time.sleep(1.5)
            print("CPU had:")
            time.sleep(1.5)
            print(cpu_card)
            print(f"Player score: {player_score}    CPU score: {cpu_score}")
            input("Press Enter to continue...")

    if player_score > cpu_score:
        input("And there's the chequered flag!")
        input(f"You clinched the championship by {player_score - cpu_score}!")
        input("And I've got to stop...")
        input("because I've got a lump in my throat...")
        input("You'll go down in history as one of the greats!")
        input("Let's hope next season's development hasn't been hurt by your tremendous championship run!")
        return

    elif player_score < cpu_score:
        input("And there's the chequered flag!")
        input(f"Your rival beat you to the championship by {cpu_score - player_score}!")
        input("That's another year of hard work ahead for you!")
        input("In the meantime, let's hope you don't get replaced by the test driver!")
        return

    else:
        input("You've tied the championship! Unheard of!")
        input("There'll be months of bickering with the FIA about this")
        input("Better just go on holiday and forget about it for a while")
        return
