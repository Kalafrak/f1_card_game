import time

def display_intro():
    print("Welcome to Apex Legacy!")
    print("Follow the prompts and try to outscore your opponent in each round.")
    print("Type 'quit' at any time to leave the game. (Real racing drivers don't quit!)")
    while True:
        user_ready = input("Are you ready to race!! (y/n)")
        if user_ready.lower() in ["quit", "exit", "n", "no"]:
            print("See ya 'round, Rookie!")
        elif user_ready.lower() in ["y", "yes"]:
            print("It's cards out and away we go!!")
            break
        print("That's not a valid input; are you sure you warmed up your tyres correctly?")

def display_round_number(round_num):
    print(f"{'*' * 50}\n{'Round ' + str(round_num):^50}\n{'*' * 50}")

def display_player_card(player_card):
    print("Your card is:")
    time.sleep(1.5)
    print(player_card)

def display_round_result(result, cpu_card, player_score, cpu_score):
    if result == "player":
        print("You win this round!")
    elif result == "cpu":
        print("Unlucky!")
    else:
        print("It's a photo finish!")
    time.sleep(1.5)
    print("CPU had:")
    time.sleep(1.5)
    print(cpu_card)
    print(f"Player score: {player_score}    CPU score: {cpu_score}")
    input("Press Enter to continue...")

def display_end_of_game(player_score, cpu_score):
    if player_score > cpu_score:
        input("And there's the chequered flag!")
        input(f"You clinched the championship by {player_score - cpu_score} points!")
        input("And I've got to stop...")
        input("because I've got a lump in my throat...")
        input("You'll go down in history as one of the greats!")
        input("Let's hope next season's development hasn't been hurt by your tremendous championship run!")
    
    elif player_score < cpu_score:
        input("And there's the chequered flag!")
        input(f"Your rival beat you to the championship by {cpu_score - player_score}!")
        input("That's another year of hard work ahead for you!")
        input("In the meantime, let's hope you don't get replaced by the test driver!")
    
    else:
        input("You've tied the championship! Unheard of!")
        input("There'll be months of bickering with the FIA about this.")
        input("Better just go on holiday and forget about it for a while.")
