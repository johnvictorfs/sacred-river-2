class User(object):
    def __init__(self, name, health, attack, defence, gold):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.gold = gold


class Enemy(object):
    def __init__(self, name, health, attack, defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence


# Class User: Name, Health, Attack, Defence, Gold
player = User('', 100, 1, 1, 5)

# Class Enemy: Name, Health, Attack, Defence
goblin_level_2 = Enemy('Goblin (Level 2)', 30, 20, 3)
goblin_level_5 = Enemy('Goblin (Level 5)', 37, 23, 4)
spider_level_1 = Enemy('Spider (Level 3)', 20, 10, 5)
spider_level_5 = Enemy('Spider (Level 5)', 25, 15, 6)
