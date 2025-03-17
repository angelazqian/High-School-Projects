import random
cardchars=['┌','─', '┐','│','░','└','┘','♠', '♥', '♣', '♦', "A " ,"2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","J ", "Q ", "K "]
value = [11,2,3,4,5,6,7,8,9,10,10,10,10]
deck = list(range (52))
random.shuffle(deck)
state = "dealcards"                                                     #will use states as finite state machine
prevstate = ""                                                          #to know the previous state
dealerhand = []
dealerprint = []
playerhand = []
playervalue = 0
dealervalue = 0
playerace = 0
dealerace = 0
choice = ""
play = True
def print_cards(cards):
    for x in range (len(cards)):
        print ("┌───────┐", end = "\t")                         #"\t" just prints out the equivalent to "tab"
    print ()
    for x in range (len(cards)):
        print ("│░░░░░░░│", end = "\t")
    print ()
    for x in range (len(cards)):
        if cards[x] == -1:
            print ("│░░░░░░░│", end = "\t")
        else: print ("│░", cardchars[(cards[x])%13 + 11], "░░░░│", end = "\t")          #is printing out the value of the card
    print ()
    for y in range (3):
        for x in range (len(cards)):
            print ("│░░░░░░░│", end = "\t")
        print ()
    for x in range (len(cards)):
        if cards[x] == -1:
            print ("│░░░░░░░│", end = "\t")
        else: print ("│░░░", cardchars[((cards[x] + 1)//13) + 7], "░░│", end = "\t")    #is printing out the suit of the card
    print ()
    for y in range (5):
        for x in range (len(cards)):
            print ("│░░░░░░░│", end = "\t")
        print ()
    for x in range (len(cards)):
        print ("└───────┘", end = "\t")
    print ()
while play:

    if state=="dealcards":                                      #dealing cards to player and dealer
        dealerhand.append(deck.pop())
        dealerhand.append(deck.pop())
        dealervalue = value[dealerhand[0]%13]+value[dealerhand[1]%13]
        dealerprint.append(-1)
        dealerprint.append(dealerhand[-1])
        if dealerhand[0]%13==0:
            dealerace += 1
        if dealerhand[1]%13==0:
            dealerace += 1
        playerhand.append(deck.pop())
        playerhand.append(deck.pop())
        if playerhand[0]%13==0:
            playerace += 1
        if playerhand[1]%13==0:
            playerace += 1
        playervalue = value[playerhand[0]%13]+value[playerhand[1]%13]
        print("Dealer's Hand:")
        print_cards(dealerprint)
        print("Player's Hand:")
        print_cards(playerhand)
        if playervalue == 21:
            state = "checkwinner"
        elif len(deck)==0:
            state = "emptydeck"
        else:
            state = "playerchoice"
        prevstate = "dealcards"
            
    elif state == "playerchoice":                               #when player making choice to either hit or stay
        choice = input("Hit or Stay? (h/s)")
        while len(choice)!=1 or choice not in "HhsS":
            choice = input("Hit or Stay? (h/s)")
        if choice in "Hh":
            state = "playerturn"
        elif choice in "Ss":
            state = "dealerturn"
        prevstate = "playerchoice"
            
    elif state == "playerturn":                                 #if player chooses to hit
        playerhand.append(deck.pop())
        playervalue += value[playerhand[-1]%13]
        print("Dealer's Hand:")
        print_cards(dealerprint)
        print("Player's Hand:")
        print_cards(playerhand)
        if playerhand[-1]%13==0:
            playerace += 1
        if playervalue > 21 and playerace > 0:
            playerace -= 1
            playervalue -= 10
        if playervalue > 21:
            state = "checkwinner"
        elif len(playerhand)>= 5:
            state = "checkwinner"
        elif len(deck)==0:
            state = "emptydeck"
        else:
            state = "playerchoice"
        prevstate = "playerturn"

    elif state == "dealerturn":                                 #if dealers turn to play
        if dealervalue < 17:
            dealerhand.append(deck.pop())
            dealervalue += value[dealerhand[-1]%13]
            dealerprint.append(dealerhand[-1])
            if dealerhand[-1]%13==0:
                dealerace += 1
            if dealervalue > 21 and dealerace > 0:
                dealervalue -= 10
                dealerace -= 1
        print("Dealer's Hand:")
        print_cards(dealerprint)
        print("Player's Hand:")
        print_cards(playerhand)
        if dealervalue > 16:
            state = "checkwinner"
        elif len(deck)==0:
            state = "emptydeck"
        prevstate = "dealerturn"

    elif state == "checkwinner":                                 #if somebody won
        if prevstate == "dealcards":                                    #if somebody got a blackjack
            if playervalue == 21:
                print ("YOU GOT A BLACKJACK! YOU WIN")
            else:
                print ("THE DEALER HAD A BLACKJACK! GAME OVER")
        elif prevstate == "playerturn":
            if playervalue > 21:
                print ("BUST! GAME OVER")
            elif len(playerhand)>=5:
                print ("FIVE CARD CHARLIE! YOU WIN")
        elif prevstate == "dealerturn":
            if dealervalue > 21:
                print ("THE DEALER BUST! YOU WIN")
            elif dealervalue > playervalue:
                print ("THE DEALER HAD A HIGHER SCORE THAN YOU! GAME OVER")
            elif dealervalue < playervalue:
                print ("YOU HAD A HIGHER SCORE THAN THE DEALER! YOU WIN")
            elif dealervalue == playervalue:
                print ("TIE GAME!")
            else:
                while True:
                    print ("You have a bug.", end = "\t")
        print("Dealer's Hand:")
        print_cards(dealerhand)
        print("Player's Hand:")
        print_cards(playerhand)
        choice = input ("Would you like to play again? (y/n)")
        while len(choice)!=1 or choice not in "YyNn":
            choice = input ("Would you like to play again? (y/n)")
        if choice in "Yy":
            state = "dealcards"
            playerhand = []
            dealerhand = []
            dealerprint = []
            playerace = 0
            dealerace = 0
            playervalue = 0
            dealervalue = 0
            if len(deck) <= 4:
                state = "emptydeck"
        else:
            play = False
                
    elif state == "emptydeck":
        print ("EMPTY DECK")
        play = False
        
            
    



















