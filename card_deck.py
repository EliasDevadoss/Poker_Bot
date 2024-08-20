import random

class CardDeck:
    
    def __init__(self):
        self.deck = [i for i in range(1, 53)]
        self.cards = [0]*9 #[flop1, flop2, flop3, turn, river, hero1, hero2, vill1, vill2]
        for i, c in enumerate(__cards):
            rand = (int)(random.random() * len(deck))
            __cards[i] = deck[rand]
            deck.pop(rand)

    number_to_name = {
        1: 'A♠️',   14: 'A♦️',  27: 'K♣️',  40: 'K♥️',
        2: '2♠️',   15: '2♦️',  28: 'Q♣️',  41: 'Q♥️',
        3: '3♠️',   16: '3♦️',  29: 'J♣️',  42: 'J♥️',
        4: '4♠️',   17: '4♦️',  30: '10♣️', 43: '10♥️',
        5: '5♠️',   18: '5♦️',  31: '9♣️',  44: '9♥️',
        6: '6♠️',   19: '6♦️',  32: '8♣️',  45: '8♥️',
        7: '7♠️',   20: '7♦️',  33: '7♣️',  46: '7♥️',
        8: '8♠️',   21: '8♦️',  34: '6♣️',  47: '6♥️',
        9: '9♠️',   22: '9♦️',  35: '5♣️',  48: '5♥️',
        10: '10♠️', 23: '10♦️', 36: '4♣️',  49: '4♥️',
        11: 'J♠️',  24: 'J♦️',  37: '3♣️',  50: '3♥️',
        12: 'Q♠️',  25: 'Q♦️',  38: '2♣️',  51: '2♥️',
        13: 'K♠️',  26: 'K♦️',  39: 'A♣️',  52: 'A♥️',
    }

    def get_value(number):
        return number_to_name.get(number, "Card value not found")

    def get_flop():
        return [get_value(__cards[0]), get_value(__cards[1]), get_value(__cards[2])]

    def get_turn():
        return [get_value(__cards[3])]

    def get_river():
        return [get_value(__cards[4])]

    def get_hero():
        return [get_value(__cards[5]), get_value(__cards[6])]

    def get_villain():
        return [get_value(__cards[7]), get_value(__cards[8])]