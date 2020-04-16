from CardList import *
from CardBuff import *
from Event import *
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
        self.cardbuffs=[]

    def initBasicBehaviours(self):
        self.cardbuffs.append(None)

    # Mulligan
    #region 
    def startMulligan(self,startCardNum):
        beforeMulliganEvent=BeforePlayerMulliganEvent(self,"BeforeMulligan",self,startCardNum)
        return self.battleGround.trigger(beforeMulliganEvent)

    def getMulliganCards(self,cardNum):
        cards=self.utils.chooseRandomFromList(self.deck.cards,cardNum)
        getMulliganCardsEvent
        cards=self.battleGround.getTrigger(self, "GetMulliganCards", self, cards)
        return cards

    def endMulligan(self,startCardNum,chosenCards):
        for card in chosenCards:
            card.moveto(self.hand.cards)
        changeNum=startCardNum-len(chosenCards)
        cards=self.utils.chooseRandomFromList(self.deck.cards,changeNum)
        for card in cards:
            card.moveto(self.hand.cards)
        self.battleGround.eventTrigger(self, "AfterMulligan", self, None)
    #endregion 
    

    def draw(self,num,sender=self):
        #this method is for direct use
        num=self.getDrawNum(sender,num,sender)
        if(self.battleGround.beforeTrigger(sender, "BeforeDraw", self, num)):
            self.battleGround.eventTrigger(sender, "OnDraw", self, num)
            self.battleGround.eventTrigger(sender, "AfterDraw", self, num)

    def getDrawNum(self,num,sender):
        num=self.battleGround.getTrigger(sender, "GetDrawNum", self, num)
    
    # TurnStart
    #region 
    def turnStart(self,sender=self):
        #this method is for direct use
        if(self.battleGround.beforeTrigger(sender, "BeforeTurnStart", self, None)):
            self.battleGround.eventTrigger(sender, "OnTurnStart", self, None)
            self.battleGround.eventTrigger(sender, "AfterTurnStart", self, None)
        self.basicTurnStart()

    def basicTurnStart(self,sender=self):
        if(self.battleGround.beforeTrigger(sender, "BeforeBasicTurnStart", self, None)):
            self.battleGround.eventTrigger(sender, "OnBasicTurnStart", self, None)
            self.battleGround.eventTrigger(sender, "AfterBasicTurnStart", self, None)
    #endregion

    # BasicBehaviour
    #region
    def BasicTurnStart(self,event):
        self.draw(1) #?number
        self.crystal.turnStart()
    def getBasicBehaviour_BasicTurnStart(self):
        cardbuff=CardBuff(player)
        cardbuff.triggers["OnBasicTurnStart"]=self.BasicTurnStart
        return cardbuff

    def BasicDraw(self,event):
        for i in range(event.value):
            card=self.deck.draw()
            card.draw()
    def getBasicBehaviour_BasicDraw(self):
        cardbuff=CardBuff(player)
        cardbuff.triggers["OnDraw"]=self.BasicDraw
        return cardbuff
    #endregion

    def trigger(self,event):
        for cardbuff in self.cardbuffs:
            cardbuff.trig(event)

    def spendCost(self,cost):
        pass

    def gameDraw(self):
        pass
    
    """description of class"""


