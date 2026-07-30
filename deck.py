import random                           #For shuffling etc.

class Deck:
    def __init__(self, drivers):
        self.cards = drivers

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            raise ValueError("Deck is empty!")
        return self.cards.pop()

    def draw_hand(self, n):
        hand = []
        for _ in range(n):
            card = self.draw()
            hand.append(card)
        return hand
    