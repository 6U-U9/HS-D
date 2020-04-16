class Event:
    def __init__(self, sender, action, target, value):
        self.sender=sender
        self.target=target
        self.action=action
        self.value=value

class GetEvent(Event):
    """get a property of target , mainly for showing, not for using"""
    def __init__(self, sender, action, target, value):
        super().__init__(sender,action,target,value)

class GetNextTurnPlayerEvent(GetEvent):
    pass
class GetMulliganCardsEvent(GetEvent):
    pass
class GetDrawNumEvent(GetEvent):
    pass
class GetFatigueDamageEvent(GetEvent):
    pass
class GetFatigueGrowthEvent(GetEvent):
    pass

class BeforeEvent(Event):
    """get a property of target"""
    def __init__(self, sender, action, target, value, permission=True):
        super().__init__(sender,action,target,value)
        self.permission=permission

class AfterEvent(Event):
    """get a property of target"""
    def __init__(self, sender, action, target, value):
        super().__init__(sender,action,target,value)

class OnEvent(Event):
    """get a property of target"""
    def __init__(self, sender, action, target, value):
        super().__init__(sender,action,target,value)

class GameEvent(Event):
    """GameBasicBehavour"""
    pass
class PlayerEvent(Event):
    pass
class UserEvent(Event):
    pass
class ObjectEvent(Event):
    """Class Cards and its subclass"""
    pass
class PlayerBasicEvent(GameEvent,PlayerEvent):
    pass


class GameInitEvent(GameEvent):
    pass
class BeforeGameInitEvent(BeforeEvent,GameInitEvent):
    pass
class OnGameInitEvent(OnEvent,GameInitEvent):
    pass
class AfterGameInitEvent(AfterEvent,GameInitEvent):
    pass

class GameStartEvent(GameEvent):
    pass
class BeforeGameStartEvent(BeforeEvent,GameStartEvent):
    pass
class OnGameStartEvent(OnEvent,GameStartEvent):
    pass
class AfterGameStartEvent(AfterEvent,GameStartEvent):
    pass

class PlayerMulliganEvent(PlayerEvent):
    pass
class BeforePlayerMulliganEvent(BeforeEvent,PlayerMulliganEvent):
    pass
class OnPlayerMulliganEvent(OnEvent,PlayerMulliganEvent):
    pass
class AfterPlayerMulliganEvent(AfterEvent,PlayerMulliganEvent):
    pass

class PlayerDrawEvent(PlayerEvent):
    pass
class BeforePlayerDrawEvent(BeforeEvent,PlayerDrawEvent):
    pass
class OnPlayerDrawEvent(OnEvent,PlayerDrawEvent):
    pass
class AfterPlayerDrawEvent(AfterEvent,PlayerDrawEvent):
    pass

class PlayerTurnStartEvent(PlayerEvent):
    pass
class BeforePlayerTurnStartEvent(BeforeEvent,PlayerTurnStartEvent):
    pass
class OnPlayerTurnStartEvent(OnEvent,PlayerTurnStartEvent):
    pass
class AfterPlayerTurnStartEvent(AfterEvent,PlayerTurnStartEvent):
    pass

class PlayerBasicTurnStartEvent(PlayerBasicEvent):
    pass
class BeforePlayerBasicTurnStartEvent(BeforeEvent,PlayerBasicTurnStartEvent):
    pass
class OnPlayerBasicTurnStartEvent(OnEvent,PlayerBasicTurnStartEvent):
    pass
class AfterPlayerBasicTurnStartEvent(AfterEvent,PlayerBasicTurnStartEvent):
    pass

class FatigueGrowEvent(PlayerBasicEvent):
    pass
class BeforeFatigueGrowEvent(BeforeEvent,FatigueGrowEvent):
    pass
class OnFatigueGrowEvent(OnEvent,FatigueGrowEvent):
    pass
class AfterFatigueGrowEvent(AfterEvent,FatigueGrowEvent):
    pass

class FatigueEvent(PlayerBasicEvent):
    pass
class BeforeFatigueEvent(BeforeEvent,FatigueEvent):
    pass
class OnFatigueEvent(OnEvent,FatigueEvent):
    pass
class AfterFatigueEvent(AfterEvent,FatigueEvent):
    pass