from random import randint
from time import sleep

money = 1000
playing = True
guess_error = False
bet_not_int = False
valid_bet = ["Heads", "Tails"]

def print_players_money():
    print("Your current balance is $" + str(money))

print_players_money()

while playing == True:
    #Getting input for what the user wants to bet on then checking to see if the input was valid
    guess = input("Do you want to bet on Heads or Tails? :")
    if guess in valid_bet:
        pass
    elif guess not in valid_bet:
        guess_error = True
        while guess_error == True:
            print("You must bet on Heads or Tails!")
            guess = input("Do you want to bet on Heads or Tails? :")
            if guess == "Heads" or guess == "Tails":
                guess_error = False
    
    #Getting value for how much the user wants to bet on there guess then checking if the bet is valid  
    bet = input("How much do you want to bet on " + guess + "? $")
    try:
        bet = int(bet)
    except:
        bet_not_int = True
        while bet_not_int == True:
            print("Your bet must be a integer!")
            bet = int(input("How much do you want to bet on " + guess + "? $"))
            try: 
                bet = int(bet)
                bet_not_int = False
            except:
                bet_not_int = True

    '''Checking users guess to see if they won or lost
    then rewarding them if they won or taking away there bet if they lost'''
    number = randint(1, 2)
    if guess == "Heads" and number == 1:
        print("The coin landed on Heads. Good guess!")
        money += bet
        print_players_money()
    elif guess == "Tails" and number == 1:
        print("The coin landed on Heads. Better luck next time!")
        money -= bet
        print_players_money()
    elif guess == "Heads" and number == 2:
        print("The coin landed on Tails. Better luck next time!")
        money -= bet
        print_players_money()
    elif guess == "Tails" and number == 2:
        print("The coin landed on Tails. Good guess!")
        money += bet
        print_players_money()