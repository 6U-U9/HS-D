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
        getMulliganCardsEvent=GetMulliganCardsEvent(self,"GetMulliganCards",self,cards)
        event=self.battleGround.trigger(getMulliganCardsEvent)
        return event.value

    def endMulligan(self,startCardNum,chosenCards):
        for card in chosenCards:
            card.moveto(self.hand.cards)
        changeNum=startCardNum-len(chosenCards)
        cards=self.utils.chooseRandomFromList(self.deck.cards,changeNum)
        for card in cards:
            card.moveto(self.hand.cards)
        afterMulliganEvent=AfterPlayerMulliganEvent(self,"AfterMulligan",self,changeNum)
        self.battleGround.trigger(afterMulliganEvent)
    #endregion 
    
    #Draw
    #region
    def draw(self,num,sender=self):
        #this method is for direct use
        #num=self.getDrawNum(sender,num,sender)
        beforePlayerDrawEvent=BeforePlayerDrawEvent(sender, "BeforePlayerDraw", self, num)
        event=self.battleGround.trigger(beforePlayerDrawEvent)
        if(event.permission):
            #self.battleGround.trigger(sender, "OnDraw", self, num)
            self.onDraw(event)
            afterPlayerDrawEvent=AfterPlayerDrawEvent(sender, "AfterPlayerDraw", self, event)
            self.battleGround.trigger(afterPlayerDrawEvent)

    def getDrawNum(self,num,sender):
        getDrawNumEvent=GetDrawNumEvent(sender,"GetDrawNum",self,num)
        event=self.battleGround.trigger(getDrawNumEvent)
        return event.value

    def onDraw(self,event):
        for i in range(event.value):
            card=self.deck.draw()

    #endregion

    # TurnStart
    #region 
    def turnStart(self,sender=self):
        #this method is for direct use
        beforePlayerTurnStartEvent=BeforePlayerTurnStartEvent(sender, "BeforePlayerTurnStart", self, None)
        event=self.battleGround.trigger(beforePlayerTurnStartEvent)
        if(event.permission):
            #self.battleGround.trigger(sender, "OnDraw", self, num)
            self.onTurnStart(event)
            afterPlayerTurnStartEvent=AfterPlayerTurnStartEvent(sender, "AfterPlayerTurnStart", self, event)
            self.battleGround.trigger(afterPlayerTurnStartEvent)
        self.basicTurnStart()

    def basicTurnStart(self,sender=self):
        beforePlayerBasicTurnStartEvent=BeforePlayerBasicTurnStartEvent(sender, "BeforePlayerBasicTurnStart", self, None)
        event=self.battleGround.trigger(beforePlayerBasicTurnStartEvent)
        if(event.permission):
            #self.battleGround.trigger(sender, "OnDraw", self, num)
            self.onBasicTurnStart(event)
            afterPlayerBasicTurnStartEvent=AfterPlayerBasicTurnStartEvent(sender, "AfterPlayerBasicTurnStart", self, event)
            self.battleGround.trigger(afterPlayerBasicTurnStartEvent)

    def onTurnStart(self):
        pass
    def onBasicTurnStart(self):
        self.draw(1) #?number
        self.crystal.turnStart()
    #endregion

    ## BasicBehaviour
    ##region
    #def BasicTurnStart(self,event):
    #    self.draw(1) #?number
    #    self.crystal.turnStart()
    #def getBasicBehaviour_BasicTurnStart(self):
    #    cardbuff=CardBuff(player)
    #    cardbuff.triggers["OnBasicTurnStart"]=self.BasicTurnStart
    #    return cardbuff

    #def BasicDraw(self,event):
    #    for i in range(event.value):
    #        card=self.deck.draw()
    #        card.draw()
    #def getBasicBehaviour_BasicDraw(self):
    #    cardbuff=CardBuff(player)
    #    cardbuff.triggers["OnDraw"]=self.BasicDraw
    #    return cardbuff
    ##endregion
    
    

    def trigger(self,event):
        for cardbuff in self.cardbuffs:
            cardbuff.trig(event)

    def spendCost(self,cost):
        pass

    def gameDraw(self):
        pass
    
    """description of class"""


