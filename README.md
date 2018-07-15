# Sacred River 2
A simple terminal text-based RPG game made in Python 3.6


***

# Preview

![Main Menu](images/preview-menu.png)

![Shop](images/preview-shop.png)

***

# Requirements

- None besides Python 3.6+, 100% Pure Python

***

# Running

- Open sacred-river folder on a terminal and do `python sacredriver.py` (`python3 sacredriver.py` on Linux) nothing special to it

***

# To do:

### Bugs:

- ~~Can only equip an item if you have more than one item in it~~ Fixed

- ~~Can only sell items if you have more than one item in it~~  Fixed

### Features:

- In-game Library with books and stuff

- ~~Add Health potion to shop~~
    - ~~Make it drinkable from inventory~~
    - ~~Make it drinkable in combat~~
    
- Add more combat functions
    - ~~Run~~
    - ~~Drink HP potions~~
    - Equip/Unequip items (possibly unnecessary)
    - Different combat stances?
        - Defensive/Aggressive/Accurate

- Add a way for user to reset save state inside the game
    - Can currently be done manually by deleting "inventory.ini" and "user_stats.ini"
    
### Code:

- Make inventory/equipment system use dictionaries for options instead of lists