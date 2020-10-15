import random 
>>>>>>> hola
money = 100

#Coin game
def coin_flip (bet, choice):
    coin_result = random.randint(1,2)
    if bet > 0 and money > 0:
        print("Please place you bet")
        print("You bet $" + str(bet))
        print("Flipping coin")
    if coin_result == 1:
        print("Heads")
    else:
        print("Tails")
    if coin_result == 1 and choice == "Heads":
        print("Coin landed on heads, you won $" + str(bet))
        return bet
    elif coin_result == 2 and choice == "Tails":
        print("Coin landed on tails, you won $" + str(bet))
        return bet
    else:
        print ("Sorry you lost. " + str(-bet))
        return -bet

#cho han game
def cho_han (bet, guess):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum_dice = dice1 + dice2
    if bet > 0 and money > 0:
        print("Please place you bet")
        print("You bet $" + str(bet) + " and you choose " + guess + ".")
        print("Rolling dices")
    if sum_dice % 2 == 0:
        print("Even")
    elif sum_dice % 2 != 0:
        print("Odd")
    if (sum_dice % 2 == 0 and guess == "Even") or (sum_dice % 2 != 0 and guess == "Odd"):
        print("Congratulations, you won $" + str(bet))
        return bet
    else:
        print ("Sorry you lost. " + str(-bet))
        return -bet

#Highest card
def high_card (bet):
    deck = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]
    p1 = deck.pop(random.randint(0, len(deck) -1))
    p2 = deck.pop(random.randint(0, len(deck) -1))
    if bet > 0 and money > 0:
        print("Please place you bet.")
        print("You bet $" + str(bet))
        print("Draw a card.")
    if p1 > p2:
        print("You draw " + str(p1) + ". CMP draw " + str(p2) + ". You win $" + str(bet))
        return bet
    elif p2 > p1:
        print("You draw " + str(p1) + ". CMP draw " + str(p2) + ". You lost $" + str(-bet))
        return -bet
    else:
        print("You draw " + str(p1) + ". CMP draw " + str(p2) + ". It's a tie")
        return 0

#Roulette
def roul(bet, choice):
    color =["Red", "Black"]
    color_result = random.choice(color)
    number = random.randint(0,37)
    bet_on = "You bet on: "
    loose = "Sorry, you lost $" + str(-bet) + "."
    win = "Congratulations you won $" + str(bet) + "."
    landing = "The ball landed on: "
    if bet > 0 and money > 0:
        print("Please place you bet.")
        print("You bet $" + str(bet))
        print("No more bets.")
        print(bet_on + str(choice))
    #Betting on color    
    if choice == "Red" and color_result == "Red":
        print(landing + color_result)
        print(win)
        return bet
    elif choice =="Black" and color_result == "Black":
        print(landing + color_result)
        print(win)
        return bet
    elif (choice == "Red" and color_result != "Red") or (choice =="Black" and color_result != "Black"):
        print(landing + color_result + ". " + loose)
        return -bet
    #Betting  Even or Odd    
    if choice == "Even" and number %2 == 0:
        print(landing + str(number))
        print(win)
        return bet
    elif choice == "Odd" and number %2 != 0:
        print(landing + str(number))
        print(win)
        return bet
        
    elif (choice == "Even" and number %2 != 0) or (choice == "Odd" and number %2 == 0):
        print(landing + str(number))
        print(loose)
        return -bet 
    #betting on number     
    if choice > 36:
        print("Choose a number between 0 and 36")
    elif choice == number:
        print(landing + str(number))
        print("Congratulations you won $" + str(bet*35) + ".")
        return bet*35
    else:
        print(landing + str(number))
        print(loose)
        return -bet
    
#Games calling
money += coin_flip(25, "Heads")
money += cho_han(35, "Odd")
money += high_card(20)
money += roul(30, "Black")
print("Total money: $" + str(money))