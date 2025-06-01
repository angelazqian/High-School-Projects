import random
import math
cardchars=["┌","─", "┐","│","░","└","┘","♠", "♥", "♣", "♦", "A " ,"2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","J ", "Q ", "K "]
finals = ["Royal Flush", "Straight Flush", "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind", "Two Pairs", "Pair", "Singles"]
value = [11,2,3,4,5,6,7,8,9,10,10,10,10]
deck = list(range (52))
straight = False
flush = False
playerfinal = 0
playerhand = []
compfinal = 0
comphand = []
playerbiggest = 0
compbiggest = 0
playerchips = 50
compchips = 50
playerbet = 0 
compbet = 0 
discards = 3
choice = ""
compchoice = 0
state = "dealcards"
play = True
gamecount = 1
biggest = 0
final = 0
notFold = True

def print_cards(cards):
  for x in range (len(cards)):
    print (x+1, "┌─────────┐", end = "\t")             #"\t" just prints out the equivalent to "tab"
  print ()
  for x in range (len(cards)):
    print ("  │░░░░░░░░░│", end = "\t")
  print ()
  for x in range (len(cards)):
    print ("  │░", cardchars[(cards[x])%13 + 11], "░░░░│", end = "\t")     #is printing out the value of the card
  print ()
  for y in range (3):
    for x in range (len(cards)):
      print ("  │░░░░░░░░░│", end = "\t")
    print ()
  for x in range (len(cards)):
    print ("  │░░░", cardchars[((cards[x])%4) + 7], "░░░│", end = "\t")  #is printing out the suit of the card
  print ()
  for y in range (5):
    for x in range (len(cards)):
      print ("  │░░░░░░░░░│", end = "\t")
    print ()
  for x in range (len(cards)):
    print ("  └─────────┘", end = "\t")
  print ()

def deal_cards(cards):
    for x in range (5):
        cards.append(deck.pop())
        
def ask_choice():
    print("If you would like to change a card, please type the number corresponding to the card you would like to discard. If not, please type '0' to continue.")
    print("Discards remaining:", discards)
    global choice 
    choice = input("Enter card number here: ")
    while len(choice)!=1 or choice not in "012345":
      choice = input("Enter card number here: ")
    if choice == "0":
      global state
      state = "betting"
    elif choice in "12345":
      state = "switchand"
      
def check_cards(cards):
    rank = []
    suit = []
    ranks = ""
    straight = False
    flush = False
    for x in range (5):
        rank.append(cards[x]%13)
        suit.append(cards[x]%4)
    rank.sort()
    if suit[0] == suit[1] == suit[2] == suit[3] == suit[4]:
      flush = True
    for x in range (5):
      ranks += str(cardchars[rank[x] + 11])
    if ranks in "A 1 2 3 4 5 6 7 8 9 10J Q K A":
      straight = True
    
    global final
    global biggest
    if straight and flush and (ranks in "10J Q K A"):
      final = 0
    elif straight and flush:
      final = 1
    elif rank[0] == rank[1] == rank[2] == rank[3] or rank[4] == rank[1] == rank[2] == rank[3]:
      final = 2
    elif (rank[0] == rank[1] == rank[2] and rank[3] == rank[4]) or (rank[4] == rank[3] == rank[2] and rank[1] == rank[0]):
      final = 3
    elif flush:
      final = 4
    elif straight:
      final = 5
    elif rank[0] == rank[1] == rank[2] or rank[3] == rank[1] == rank[2] or rank[4] == rank[3] == rank[2]:
      final = 6
    elif (rank[0] == rank[1] and rank[2] == rank[3]) or (rank[0] == rank[1] and rank[4] == rank[3]) or (rank[2] == rank[1] and rank[4] == rank[3]):
      final = 7
    elif rank[0] == rank[1] or rank[2] == rank[1] or rank[2] == rank[3] or rank[3] == rank[4]:
      final = 8
    else:
      final = 9
    biggest = rank[4]
    if (rank[0] == 1):
        biggest = 14

while play:
    
  if state == "dealcards":              #deals the cards of both the comp and the player
    print ("Game ", gamecount)
    deck = list(range(52))
    random.shuffle(deck)
    playerhand = []
    comphand = []
    deal_cards(comphand)
    deal_cards(playerhand)
    print ("Your hand:")
    discards = 3
    print_cards(playerhand)
    ask_choice()
 
  if state == "switchand":              #changes the player's hand based on the choice
    playerhand[ord(choice)-49] = deck.pop()
    discards -= 1
    print ("switchand")
    if discards == 0:
      state = "betting"
    if state == "switchand":
      print("Your hand:")
      print_cards(playerhand)
      ask_choice()
 
  if state == "betting":
    check_cards(playerhand)
    playerfinal = final
    playerbiggest = biggest
    check_cards(comphand)
    compfinal = final
    notFold = True
    compbiggest = biggest
    if (choice != "0"):
        print("Your hand: ")
        print_cards(playerhand)
    print(finals[playerfinal])
    compbet = 1
    print("Your chips: ", playerchips)
    print("Computer's chips: ", compchips)
    if gamecount%2 == 1:
        print ("You go first! If you would like to fold and lose 1 token to move on to the next hand, please type '0'. If you would like to make a bet, please type in the number of tokens you are wagering. You may not bet more tokens than you have.")
        playerbet = int(input("How much do you bet? "))
        if playerbet == 0:
            playerchips -= 1 
            compchips += 1 
            notFold = False
            print ("Moving on to next round")
        elif playerbet > playerchips:
            playerbet = playerchips
        if notFold:
            if compfinal == 0:
                print ("Your opponent bets 1 token.")
            else:
                print ("Your opponent folds! You gain 1 token and move to the next hand.")
                playerchips += 1 
                compchips -= 1 
                notFold = False
    else:
        if (compfinal == 0):
            print ("The opponent starts and bets ", compbet, " tokens. If you would like to fold and lose 1 token to move on to the next hand, please type '0'. If you would like to make a bet, please type in the number of tokens you are wagering. You may not bet more tokens than you have.")
            playerbet = int(input("How much do you bet? "))
            if playerbet == 0:
                playerchips -= 1 
                compchips += 1 
                notFold = False
                print ("Moving on to next round")
            elif playerbet > playerchips:
                playerbet = playerchips
        else: 
            print ("Your opponent goes first and folds! You gain 1 token and move to the next hand.")
            playerchips += 1 
            compchips -= 1 
            notFold = False
    if notFold:
        print ("Computer's hand: ")
        print_cards(comphand)
        print(finals[compfinal])
        if (playerfinal < compfinal):
            print ("Player wins!")
            playerchips += compbet
            compchips -= compbet 
        elif (playerfinal > compfinal):
            print ("Computer wins!")
            playerchips -= playerbet 
            compchips += playerbet
        elif (playerfinal == compfinal):
            if (playerbiggest > compbiggest):
                print ("Player wins!")
                playerchips += compbet
                compchips -= compbet 
            elif (playerbiggest < compbiggest):
                print ("Computer wins!")
                playerchips -= playerbet 
                compchips += playerbet
            else: 
                print ("Draw!")
    state = "dealcards"
    gamecount += 1
    if (compchips == 0):
        print ("You win the game!")
    elif (playerchips == 0):
        print ("you somehow lost against a bot that randomly generates everything lmao")
    if (compchips * playerchips == 0):
        play = False
 
 
 
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      

