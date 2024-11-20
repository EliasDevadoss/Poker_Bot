import streamlit as st

class Chips:
    
    def __init__(self):
        self.hero_stack = 100
        self.villain_stack = 100
        self.hero_bet = 0
        self.villain_bet = 0
        self.pot = 0

    def get_hero(self):
        return self.hero_stack
    
    def get_villain(self):
        return self.villain_stack
    
    def get_hero_bet(self):
        return self.hero_bet
    
    def get_villain_bet(self):
        return self.villain_bet
    
    def get_pot(self):
        return self.pot
    
    def bet_hero(self, betSize):
        if betSize > self.hero_stack:
            self.hero_bet = self.hero_stack
            self.pot = self.pot + self.hero_stack
            self.hero_stack = 0
        else:
            self.hero_bet = betSize
            self.hero_stack = self.hero_stack - betSize
            self.pot = self.pot + betSize

    def bet_villain(self, betSize):
        if betSize > self.villain_stack:
            self.villain_bet = self.villain_stack
            self.pot = self.pot + self.villain_stack
            self.villain_stack = 0
        else:
            self.villain_bet = betSize
            self.villain_stack = self.villain_stack - betSize
            self.pot = self.pot + betSize

    def call_hero(self):
        self.bet_hero(self.villain_bet)
        self.villain_bet = 0
    
    def call_villain(self):
        self.bet_villain(self.hero_bet)
        self.hero_bet = 0
    
    def raise_hero(self, val = 0):
        if val != 0:
            newBet = val
        else:
            newBet = self.villain_bet * 3
        if newBet > self.hero_stack:
            self.hero_bet = self.hero_stack - self.villain_bet
            self.pot = self.pot + self.hero_stack
            self.hero_stack = 0
        else:
            self.hero_bet = newBet - self.villain_bet # Would need to be changed if stacks were unequal size in case of all-in
            self.hero_stack = self.hero_stack - newBet
            self.pot = self.pot + newBet
    
    def raise_villain(self, val = 0):
        if val != 0:
            newBet = val
        else:
            newBet = self.hero_bet * 3
        if newBet > self.villain_stack:
            self.villain_bet = self.villain_stack - self.hero_bet
            self.pot = self.pot + self.villain_stack
            self.villain_stack = 0
        else:
            self.villain_bet = newBet - self.hero_bet # Would need to be changed if stacks were unequal size in case of all-in
            self.villain_stack = self.villain_stack - newBet
            self.pot = self.pot + newBet
