from CardList import *
class Player:
    """actually the side of the game, not an entity in the game
    save the state; deal with crystals and aura effects"""
    def __init__(self, initDeck, utils, battleGround):
        self.initDeck=initDeck  #class DefaultDeck
        self.battleGround=battleGround
        self.deck=self.initDeck.getDeck()
        self.hero=self.initDeck.getHero()
        self.hand=CardList()
        self.board=CardList()
        #self.weapon=[]
        self.graveyard=CardList()
        self.secrets=CardList()
        self.utils=utils
        self.crystal=[]

    def startMulligan(self,startCardNum):
        cards=self.utils.chooseRandomFromList(self.deck.cards,startCardNum)
        return cards

    def endMulligan(self,startCardNum,chosenCards):
        for card in chosenCards:
            card.moveto(self.hand.cards)
        changeNum=startCardNum-len(chosenCards)
        cards=self.utils.chooseRandomFromList(self.deck.cards,changeNum)
        for card in cards:
            card.moveto(self.hand.cards)

    def turnStart(self):
        pass

    def spendCost(self,cost):
        pass

    def gameDraw(self):
        pass
    
    """description of class"""


