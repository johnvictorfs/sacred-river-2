# Local
from clear import clear_screen
from prompt import prompt


class Player(object):

    def __init__(self, name, attack, defence, health, gold):
        self.name = name
        self.attack = int(attack)
        self.defence = int(defence)
        self.health = int(health)
        self.gold = int(gold)

    def display(self):
        clear_screen()
        print(f"""
--- Displaying stats of {self.name} ---
- Attack: {self.attack}
- Defence: {self.defence}
- Health: {self.health}
- Gold: {self.gold}
-------
        """)
        prompt()


def death():
    clear_screen()
    print(f"""
--- Oh dear, you're dead! ---

Restart the game to keep playing, your stats will be reset :/)

---
    """)
    prompt("< Press Enter to exit. >")
    exit(0)

