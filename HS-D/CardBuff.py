class CardBuff:
    """method of (get property) and (callbacks)"""
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
    def __init__(self,holder):
        self.counter=[]
        self.triggers={}
        self.holder=holder

    def trig(self,event):
        if(not event.action in self.triggers.keys()):
            return
        self.triggers[event.action](event)

    def isTarget(self,card):
        return True

