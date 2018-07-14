# Local
from clear import clear_screen
from prompt import prompt


class Player(object):

    def __init__(self, name, attack, defence, health, gold, max_health=50):
        self.name = name
        self.attack = int(attack)
        self.defence = int(defence)
        self.health = int(health)
        self.gold = int(gold)
        self.max_health = int(max_health)

    def display_stats(self):
        clear_screen()
        print(f"""
_________________________________________
||| Displaying stats of {self.name} |||
- Attack: {self.attack}
- Defence: {self.defence}
- Health: {self.health}/{self.max_health}
- Gold: {self.gold}
_________________________________________
        """)
        prompt()

    def death(self):
        clear_screen()
        print(f"""
    --- Oh dear, {self.name} Died! ---
    
    Restart the game to keep playing, your stats will be reset :/)
    
    ---
        """)
        prompt("< Press Enter to exit. >")
        exit(0)

