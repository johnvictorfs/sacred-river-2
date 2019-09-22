from dataclasses import dataclass


@dataclass
class Item:
    name: str
    buy_value: int = 0
    sell_value: int = 0
    sellable: bool = False
    quantity: int = 1

    def is_sellable(self) -> str:
        return 'Yes' if self.sellable else 'No'

    def __str__(self) -> str:
        return f"[Name] {self.name}\n[Buy Value] {self.buy_value}\n[Sell Value] {self.sell_value}\n[Sellable?] {self.is_sellable()}"


@dataclass
class Potion(Item):
    pass


@dataclass
class Equipment(Item):
    pass


@dataclass
class Weapon(Equipment):
    attack: int = 0

    def __str__(self) -> str:
        return super.__str__() + f'\n[Attack] +{self.attack}'


@dataclass
class Armour(Equipment):
    defence: int = 0

    def __str__(self) -> str:
        return super.__str__() + f'\n[Defence] +{self.defence}'


@dataclass
class HealthPotion(Potion):
    name: str = 'Health Potion'
    heal_value: int = 10
    buy_value: int = 6

    def __str__(self) -> str:
        return super.__str__() + f'\n[Heal Value] +{self.heal_value}'


@dataclass
class EnhancedHealthPotion(HealthPotion):
    name: str = 'Enhanced Health Potion'
    heal_value: int = 20
    buy_value: int = 11
