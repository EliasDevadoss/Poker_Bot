
class Chips:
    
    def __init__(self):
        self.hero_stack = 100
        self.villain_stack = 100
        self.pot = 0

    def get_hero(self):
        return self.hero_stack
    
    def get_villain(self):
        return self.villain_stack
    
    def get_pot(self):
        return self.pot