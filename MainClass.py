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
print(i)
print(str(player1.thename) + " rolled a " + str(slam) + ". This will be the slam value for the rest of the game.")

a = 0
i = 0
while a <= 0 :
    temp1 = die1.__roll__()
    print(str(playerList[i].thename) + " rolled a " + str(slam) + ". This will be the slam value for the rest of the game.")
    temp2 = die1.__roll__()
    print(str(playerList[i].thename) + " rolled a " + str(slam) + ". This will be the slam value for the rest of the game.")
    temp3 = die1.__roll__()
    print(str(playerList[i].thename) + " rolled a " + str(slam) + ". This will be the slam value for the rest of the game.")
    if (temp1 != slam and temp2 != slam and temp3 != slam) :
        a = a + 1
    
