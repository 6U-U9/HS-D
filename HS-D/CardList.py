class CardList():
    def __init__(self,cards=[]):
        self._cards=cards

    def get(self):
        return self._cards

    @property
    def cards(self):
        return self._cards

    def length(self):
        return len(self.cards)