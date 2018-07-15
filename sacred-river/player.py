import random

# Local
from clear import clear_screen
from prompt import prompt


class Player(object):

    def __init__(self, name, attack, defence, health, gold, luck, max_health=50):
        self.name = name
        self.attack = int(attack)
        self.defence = int(defence)
        self.health = int(health)
        self.gold = int(gold)
        self.luck = int(luck)
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
- Luck: {self.luck}

(Higher Luck = Increased chance of running
away from monsters and unique drops)
_________________________________________""")
        prompt()

    def level_up(self, skill, chance, increase, message=True):
        """
        Tries to level up 'skill' (can be 'attack', 'defence', 'health' or 'luck'.

        Rolls random between 1 and 'chance', if roll is equal to 'chance', skill levels up.
        Increase is a random roll between 1 and 'increase'

        :param skill: str
        :param chance: int
        :param increase: int
        :param message: bool
        :return: None
        """
        skills = {
            'attack': (self.attack, "Attack"),
            'defence': (self.defence, "Defence"),
            'health': (self.max_health, "HP"),
            'luck': (self.luck, "Luck")
        }

        roll = random.randint(0, chance)

        if chance is roll:
            final_increase = random.randint(1, increase)
            difference = skills[skill][0] - final_increase
            skills[skill][0] += final_increase

            skill_name = skills[skill][1]
            skill_level = skills[skill][0]

            if message is True:
                print(f"\n** LEVEL UP: Your {skill_name} has increased by {difference} and is now {skill_level}. **")

    def death(self):
        clear_screen()
        print(f"""
    --- Oh dear, {self.name} Died! ---
    
    Restart the game to keep playing.
    Your stats will keep going from the last point you saved.
    
    ---""")
        prompt("< Press Enter to exit. >")
        exit(0)

