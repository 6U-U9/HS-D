from Player import *
from Event import *
import Utils
MAX_TURN_NUM=30

class BattleGround:
    """description of class"""
    def __init__(self, initDecks):
        self.initDecks=initDecks
        self.triggers={}
        self.players=[]
        self.utils=Utils.Utils()
        self.order=[]
        #self.turnSeq=[]
        self.onPlayPlayer=None
        self.logs=[]
        self.entities=[]
        
    def initGame(self):
        for deck in self.initDecks:
            self.players.append(Player(deck)) 
        self.genTurnOrder()

    def gameStart(self):
        beforeGameStartEvent=BeforeGameStartEvent(self,"BeforeGameStart",self,None)
        event=self.trigger(self, beforeGameStartEvent)
        if(event.permission):
            self.onGameStart()
            afterGameStartEvent=AfterGameStartEvent(self,"AfterGameStart",self,None)
            self.trigger(self, afterGameStartEvent)

    def mulligan(self):
        for player in self.players:
            if(self.order.index(player)==0):
                event1=player.startMulligan(3)
            if(self.order.index(player)==1):
                event2=player.startMulligan(4)
                #player.hand.cards.append("Coin")
        #wait for choose
        for player in self.players:
            player.endMulligan()

    def nextTurn(self):
        player=self.getNextTurnPlayer()
        self.onPlayPlayer=player
        player.turnStart()

    def genTurnOrder(self):
        self.order=utils.shuffle(players)
        #self.turnSeq=self.order*MAX_TURN_NUM

    def getNextTurnPlayer(self):
        if(onPlayPlayer==None):
            nextTurnPlayer=self.order[0]
        else:
            i=self.order.index(onPlayPlayer)
            if (i<len(self.order)):
                nextTurnPlayer=self.order[i+1]
            else:
                nextTurnPlayer=self.order[0]
        getNextTurnPlayer=GetNextTurnPlayerEvent(self,"GetNextTurnPlayer",self, nextTurnPlayer)
        event=self.trigger(event)
        return event.value


    def trigger(self, event):
        for entity in self.entities:
            event=entity.trigger(event)
        return event

    #def eventTrigger(self, event):
    #    for entity in self.entities:
    #        event=entity.trigger(event)
    #    return event

    #def beforeTrigger(self, event):
    #    for entity in self.entities:
    #        event=entity.trigger(event)
    #    return event
    #    return permission #bool, which indicates whether the action should go on 

    def getChosenObject(self):
        return []

    def gameEnd(self):
        pass

