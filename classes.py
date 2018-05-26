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


class Item(object):
    def __init__(self, name, attack, armour, buy_value, sell_value, heal):
        self.name = name
        self.attack = attack
        self.armour = armour
        self.buy_value = buy_value
        self.sell_value = sell_value
        self.heal = heal


# Class User: Name, Health, Attack, Defence, Gold #
player = User('', 100, 1, 1, 5)

# Class Enemy: Name, Health, Attack, Defence #
goblin_level_2 = Enemy('Goblin (Level 2)', 30, 20, 3)
goblin_level_5 = Enemy('Goblin (Level 5)', 37, 23, 4)
spider_level_1 = Enemy('Spider (Level 3)', 20, 10, 5)
spider_level_5 = Enemy('Spider (Level 5)', 25, 15, 6)

# Class Item: Name, Attack, Armour, Buy Value, Sell Value, Heal #
# Sell Value = 50% of Buy Value (rounded down)

# Weapons #
iron_sword = Item('Iron Sword', 5, 0, 8, 4, 0)
steel_sword = Item('Steel Sword', 8, 0, 12, 6, 0)

# Potions #
health_potion = Item('Health Potion', 0, 0, 5, 2, 20)
