import random

class Die :

    def __init__( self, sides ) :
        self.thesides = 6

    def __str__( self ) :
        return "This die has " + str(self.thesides) + " sides."

    def __roll__( self ) :
        return random.randrange(1, self.thesides+1, 1)

class Player :
    
    def __init__ (self, name, score) :
        self.thename = name
        self.thescore = 0

    def __str__ ( self ) :
        return "This player's name is " + str(self.thename) + " and they have " + str(self.thescore) + " points."

    def __giveSlamPoints__ ( self ) :
        self.thescore = self.thescore + 1

#name = input("Name?")
die1 = Die(6)
player1 = Player("Billy", 0)
player2 = Player("Bob", 0)
player3 = Player("Joe", 0)

playerList = [player1, player2, player3]

slam = (die1.__roll__())
print(str(player1.thename) + " rolled a " + str(slam) + ". This will be the slam value for the rest of the game...")


#i is current player
i = 0
while player1.thescore < 15 and player2.thescore < 15 and player3.thescore < 15:
    oldscore = playerList[i].thescore
    temp1 = die1.__roll__()
    print(str(playerList[i].thename) + " rolled a " + str(temp1) + " on roll 1.")
    temp2 = die1.__roll__()
    print(str(playerList[i].thename) + " rolled a " + str(temp2) + ". on roll 2.")
    temp3 = die1.__roll__()
    print(str(playerList[i].thename) + " rolled a " + str(temp3) + ". on roll 3.")
    if (temp1 == slam and temp2 == slam and temp3 == slam) :
        playerList[i].thescore = playerList[i].thescore + 15
        print(str(playerList[i].thename) + " rolled a grand slam for 15 points!")
        print("Their score is now " + str(playerList[i].thescore))
    elif ((temp1 == slam and temp2 == slam) or (temp2 == slam and temp3 == slam) or (temp3 == slam and temp1 == slam)) :
        playerList[i].thescore = playerList[i].thescore + 5
        print(str(playerList[i].thename) + " rolled a small slam for 5 points!")
        print("Their score is now " + str(playerList[i].thescore))
    elif (temp1 == slam or temp2 == slam or temp3 == slam) :
        playerList[i].thescore = playerList[i].thescore + 1
        print(str(playerList[i].thename) + " got 1 point!")
        print("Their score is now " + str(playerList[i].thescore))
    else :
        if i == 2:
            i = 0
        else :
            i = i + 1

if player1.thescore > player2.thescore and player1.thescore > player3.thescore :
    print(player1.thename + " got out!")
elif player2.thescore > player1.thescore and player2.thescore > player3.thescore :
    print(player2.thename + " got out!")
else :
    print(player3.thename + " got out!")
