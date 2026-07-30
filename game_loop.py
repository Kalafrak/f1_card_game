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
        print("Bye then, Rookie!")
        return

#Main game loop
    player_score = 0
    cpu_score = 0
    for round_num in range(1, 11):                                          #10 round game length
        print(f"{'*' * 50}\n{'Round ' + str(round_num):^50}\n{'*' * 50}")   #Print round number
        player_card = deck.draw()                                           #Draw player's card
        cpu_card = deck.draw()                                              #Draw cpu's card
        print("Your card is:")
        time.sleep(1.5)
        print(player_card)
        player_chosen_stat = input("Choose a stat to attack with (ta/lo/ag/mo/hu/sc)")                  #Get stat choice from player and compare with cpu_card

        if player_chosen_stat.lower() in ["ta", "talent"]:                                        
            if player_card.talent > cpu_card.talent:
                print("You win this round!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                player_score += player_card.talent - cpu_card.talent
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")
            if player_card.talent < cpu_card.talent:
                print("Unlucky!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                cpu_score += cpu_card.talent - player_card.talent
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")
            if player_card.talent == cpu_card.talent:
                print("It's a photo finish!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")

        elif player_chosen_stat.lower() in ["lo", "longevity"]:                                        
            if player_card.longevity > cpu_card.longevity:
                print("You win this round!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                player_score += player_card.longevity - cpu_card.longevity
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")
            if player_card.longevity < cpu_card.longevity:
                print("Unlucky!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                cpu_score += cpu_card.longevity - player_card.longevity
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")
            if player_card.longevity == cpu_card.longevity:
                print("It's a photo finish!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")

        elif player_chosen_stat.lower() in ["ag", "aggression"]:                                        
            if player_card.aggression > cpu_card.aggression:
                print("You win this round!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                player_score += player_card.aggression - cpu_card.aggression
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")
            if player_card.aggression < cpu_card.aggression:
                print("Unlucky!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                cpu_score += cpu_card.aggression - player_card.aggression
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")
            if player_card.aggression == cpu_card.aggression:
                print("It's a photo finish!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")

        elif player_chosen_stat.lower() in ["mo", "moxie"]:                                        
            if player_card.moxie > cpu_card.moxie:
                print("You win this round!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                player_score += player_card.moxie - cpu_card.moxie
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")
            if player_card.moxie < cpu_card.moxie:
                print("Unlucky!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                cpu_score += cpu_card.moxie - player_card.moxie
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")
            if player_card.moxie == cpu_card.moxie:
                print("It's a photo finish!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")

        elif player_chosen_stat.lower() in ["hu", "humour"]:                                        
            if player_card.humour > cpu_card.humour:
                print("You win this round!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                player_score += player_card.humour - cpu_card.humour
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")
            if player_card.humour < cpu_card.humour:
                print("Unlucky!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                cpu_score += cpu_card.humour - player_card.humour
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")
            if player_card.humour == cpu_card.humour:
                print("It's a photo finish!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")

        elif player_chosen_stat.lower() in ["sc", "scrupulousness"]:                                        
            if player_card.scrupulousness > cpu_card.scrupulousness:
                print("You win this round!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                player_score += player_card.scrupulousness - cpu_card.scrupulousness
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")
            if player_card.scrupulousness < cpu_card.scrupulousness:
                print("Unlucky!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                cpu_score += cpu_card.scrupulousness - player_card.scrupulousness
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")
            if player_card.scrupulousness == cpu_card.scrupulousness:
                print("It's a photo finish!")
                time.sleep(1.5)
                print("CPU had:")
                time.sleep(1.5)
                print(cpu_card)
                time.sleep(1.5)
                print(f"Player score: {player_score}    CPU score: {cpu_score}")
                input("Press Enter to continue...")

        elif player_chosen_stat.lower() in ["quit", "exit"]:
            print("Bye then, Rookie!")
            return

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
