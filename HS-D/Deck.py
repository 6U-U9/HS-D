import CardList
from Utils import *
class Deck(CardList.CardList):
    """description of class"""
    def __init__(self,cards,player,fatigue=0):
        super().__init__(cards)
        self.player=player
        self.maxCards=60
        self._fatigue=_Int(fatigue)
        self.cardbuffs=[]

    
    def draw(self):
        if(len(self._cards)>0):
            self._cards[0].draw()
        else:
            self.fatigue()

    def shuffle(self):
        self._cards=self._cards

    def fatigue(self,sender=self):
        if(self.battleGround.beforeTrigger(sender, "BeforeFatigue", target, damage)):
            self.battleGround.eventTrigger(sender, "OnFatigue", target, damage)
            self.battleGround.eventTrigger(sender, "AfterFatigue", target, damage)

    def fatigueGrow(self,sender=self):
        if(self.battleGround.beforeTrigger(sender, "BeforeFatigueGrow", target, delta)):
            self.battleGround.eventTrigger(sender, "OnFatigueGrow", target, delta)
            self.battleGround.eventTrigger(sender, "AfterFatigueGrow", target, delta)

    def getFatigueDamage(self,sender):
        damage=self._fatigue
        return damage
    #def getFatigueTarget(self,sender):
    #    target=self.player.getHero()
    #    return target

    def getFatigueGrowth(self,sender):
        delta=1 #?num
        return delta
    #def getFatigueGrowTarget(self,sender):
    #    target=self._fatigue
    #    target=self.battleGround.getTrigger(sender, "GetFatigueGrowTarget", self, target)
    #    return target

     # BasicBehaviour
    #region
    def BasicFatigue(self,event):
        event.target.takeDamage(event.value)
    def getBasicBehaviour_Fatigue(self):
        cardbuff=CardBuff(self.player)
        cardbuff.triggers["OnFatigue"]=self.BasicFatigue
        return cardbuff

    def BasicFatigueGrow(self,event):
        target=target+value
    def getBasicBehaviour_FatigueGrow(self):
        cardbuff=CardBuff(self.player)
        cardbuff.triggers["OnFatigueGrow"]=self.BasicFatigueGrow
        return cardbuff
    #endregion
    
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
    