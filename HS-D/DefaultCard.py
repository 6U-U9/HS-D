from BasicCard import *
class DefaultCard(BasicCard):
    """Card in Collection(even if cannot be collected)
       generate Card is based on this class"""
    def __init__(self, id, rarity, name, cardclass, cost, cardbuff, player):
        self.rarity=rarity
        self.name=name
        self.cardclass=cardclass
        return super().__init__(id, rarity, name, cardclass, cost, cardbuff, player)
    
    def addtoDeck(self):
        pass

    def getEntity(self):
        pass