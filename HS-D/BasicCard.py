class BasicCard:
    """Basic of Card:it defines basic actions
       actions here will not trigger any thing, so please be cardful to use the methods here"""
    def __init__(self, id, cost, cardbuff, player):
        self.id=id
        self.cost=cost
        self.cardbuff=cardbuff
        self.player=player
        self.effect={}#trigger name:CardBuff

        #beforeSomething
        #onSomething
        #afterSomething
        #beforeGameStart
        #onGameStart（决定先后手）
        #afterGameStart
        #StartHand（换牌）
        #TurnStart（获得水晶，,刷新水晶，刷新攻击次数，抽牌）
            #Draw
                #Fatigue
                #HandFull
            #GainAttackChance
            #GainCrystal
            #FreshCrystal
        #CardPlay
            #SpendCrystal
            #SummonMinion
        #Attack
            #ChosenAsTarget
        #Damaged
            #HeroDamaged
        #DealDamage
        #Dead
        #Kill
        #TurnEnd
        #beforeGameEnd
        #onGameEnd
        #afterGameEnd

    def getCard(self):
        return None

    def getCopy(self):
        return None

    def getCost(self):
        return self.cost

    def getBattleGround(self):
        return self.player.getbattleGround()

    def getPlayer(self):
        return self.player

    def getLocation(self):
        battleGround=self.getBattleGround()
        return battleGround.getLocation(self)

    def moveto(self,location,position=None):
        pastLocation=self.getLocation()
        pastLocation.remove(self)
        if(position==None):
            location.append(self)
        else:
            location.append(self,position)


    def play(self,target=None):
        self.player.spendCost(self.cost)
        pass

    def attack(self,target=None):
        pass

        


