import random

class CardDeck:

    number_to_name = {
        1: 'A♠️',   14: 'A♦️',  27: 'K♣️',  40: 'K♥️',
        2: '2♠️',   15: '2♦️',  28: 'Q♣️',  41: 'Q♥️',
        3: '3♠️',   16: '3♦️',  29: 'J♣️',  42: 'J♥️',
        4: '4♠️',   17: '4♦️',  30: 'T♣️',  43: 'T♥️',
        5: '5♠️',   18: '5♦️',  31: '9♣️',  44: '9♥️',
        6: '6♠️',   19: '6♦️',  32: '8♣️',  45: '8♥️',
        7: '7♠️',   20: '7♦️',  33: '7♣️',  46: '7♥️',
        8: '8♠️',   21: '8♦️',  34: '6♣️',  47: '6♥️',
        9: '9♠️',   22: '9♦️',  35: '5♣️',  48: '5♥️',
        10: 'T♠️',  23: 'T♦️',  36: '4♣️',  49: '4♥️',
        11: 'J♠️',  24: 'J♦️',  37: '3♣️',  50: '3♥️',
        12: 'Q♠️',  25: 'Q♦️',  38: '2♣️',  51: '2♥️',
        13: 'K♠️',  26: 'K♦️',  39: 'A♣️',  52: 'A♥️',
    }

    def __init__(self):
        self.deck = [i for i in range(1, 53)]
        self.cards = [0]*9 #[flop1, flop2, flop3, turn, river, hero1, hero2, vill1, vill2]
        for i, c in enumerate(self.cards):
            rand = (int)(random.random() * len(self.deck))
            self.cards[i] = self.deck[rand]
            self.deck.pop(rand)

    def get_value(self, number):
        return self.number_to_name.get(number, "Card value not found")

    def get_flop(self):
        return [self.get_value(self.cards[0]), self.get_value(self.cards[1]), self.get_value(self.cards[2])]

    def get_turn(self):
        return [self.get_value(self.cards[3])]

    def get_river(self):
        return [self.get_value(self.cards[4])]

    def get_hero(self):
        return [self.get_value(self.cards[5]), self.get_value(self.cards[6])]

    def get_villain(self):
        return [self.get_value(self.cards[7]), self.get_value(self.cards[8])]