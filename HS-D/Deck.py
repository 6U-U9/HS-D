import CardList
from Event import *
from Utils import *
class Deck(CardList.CardList):
    """description of class"""
    def __init__(self,cards,player,fatigue=0):
        super().__init__(cards)
        self.player=player
        self.maxCards=60#?num
        self._fatigue=_Int(fatigue)
        #self.cardbuffs=[]

    
    def draw(self):
        if(len(self._cards)>0):
            self._cards[0].draw()
        else:
            self.fatigue()

    def shuffle(self):
        self._cards=self._cards

    def fatigue(self,sender=self):
        self.fatigueGrow()
        beforeFatigueEvent=BeforeFatigueEvent(sender, "BeforeFatigue", self.player.getHero(), self._fatigue)
        event=self.battleGround.trigger(beforeFatigueEvent)
        if(event.permission):
            #self.battleGround.trigger(sender, "OnDraw", self, num)
            self.onFatigue(event)
            afterFatigueEvent=AfterFatigueEvent(sender, "AfterFatigue", self.player.getHero(), event)
            self.battleGround.trigger(afterFatigueEvent)

    def fatigueGrow(self,sender=self):
        beforeFatigueGrowEvent=BeforeFatigueGrowEvent(sender, "BeforeFatigueGrow", self, 1)#?num
        event=self.battleGround.trigger(beforeFatigueGrowEvent)
        if(event.permission):
            #self.battleGround.trigger(sender, "OnDraw", self, num)
            self.onFatigueGrow(event)
            afterFatigueGrowEvent=AfterFatigueGrowEvent(sender, "AfterFatigueGrow", self, event)
            self.battleGround.trigger(afterFatigueGrowEvent)
    
    def onFatigue(self,event):
        event.target.takeDamage(event.value)

    def onFatigueGrow(self,event):
        self._fatigue=self._fatigue+event.value

    def getFatigueDamage(self,sender):
        damage=self._fatigue
        getFatigueDamageEvent=GetFatigueDamageEvent(sender,"GetFatigueDamage",self.player.getHero(),damage)
        event=self.battleGround.trigger(getFatigueDamageEvent)
        return event.value

    def getFatigueGrowth(self,sender):
        delta=1#?num
        getFatigueGrowthEvent=GetFatigueGrowthEvent(sender,"GetFatigueGrowth",self,delta)
        event=self.battleGround.trigger(getFatigueGrowthEvent)
        return event.value

    # # BasicBehaviour
    ##region
    #def BasicFatigue(self,event):
    #    event.target.takeDamage(event.value)
    #def getBasicBehaviour_Fatigue(self):
    #    cardbuff=CardBuff(self.player)
    #    cardbuff.triggers["OnFatigue"]=self.BasicFatigue
    #    return cardbuff

    #def BasicFatigueGrow(self,event):
    #    target=target+value
    #def getBasicBehaviour_FatigueGrow(self):
    #    cardbuff=CardBuff(self.player)
    #    cardbuff.triggers["OnFatigueGrow"]=self.BasicFatigueGrow
    #    return cardbuff
    ##endregion
    
    #def getLength(self,sender=None):
    #    length=len(self.cards)
    #    if(sender==None):
    #        sender=self.player
    #    length=self.player.battleGround.getTrigger(sender, "GetDeckLength", self, length)
    #    return length
    
    #def getTopCard(self,sender=None):
    #    card=self.cards[0]
    #    card=self.player.battleGround.getTrigger(sender, "GetDeckTopDeck", self, card)
    #    return card
    