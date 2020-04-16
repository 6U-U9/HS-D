class Event:
    def __init__(self, sender, action, target, value):
        self.sender=sender
        self.target=target
        self.action=action
        self.value=value

class GetEvent(Event):
    """get a property of target"""
    def __init__(self, sender, action, target, value):
        super().__init__(sender,action,target,value)

class GetNextTurnPlayerEvent(GetEvent):
    pass
class GetMulliganCardsEvent(GetEvent):
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
    pass
class PlayerEvent(Event):
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


