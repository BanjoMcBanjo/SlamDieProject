import random

class Die :

    def __init__( self, sides ) :
        self.thesides = 6

    def __str__( self ) :
        return "This die has " + str(self.thesides) + " sides."

    def __roll__( self ) :
        return random.randrange(1, self.thesides+1, 1)
