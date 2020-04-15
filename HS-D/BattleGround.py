from Player import *
import Utils
MAX_TURN_NUM=30

class BattleGround:
    """description of class"""
    def __init__(self, initDecks):
        self.initDecks=initDecks
        self.triggers={}
        self.players=[]
        self.utils=Utils.Utils()
        for deck in self.initDecks:
            self.players.append(Player(deck)) 
        self.turnSeq=[]
        self.player_OnPlay=None
        self.logs=[]
        
    def gameStart(self):
        for player in self.players:
            player.mulligan()

    def nextTurn(self):
        if(len(self.turnSeq)==0):
            for player in self.players:
                player.gameDraw()
            return
        player=self.turnSeq.pop[0]
        player.turnStart();
        self.player_OnPlay=player

    def genTurnSeq(self):
        order=utils.shuffle(players)
        self.turnSeq=order*MAX_TURN_NUM

    def getChosenObject(self):
        return []

    def gameEnd(self):
        pass

