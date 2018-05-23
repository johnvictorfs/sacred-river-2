from continueScreen import continueScreen


class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item
        print('Added {} to inventory.'.format(item.name))

    def print_items(self):
        for item in self.items.values():
            print('Name: {}'.format(item.name))
            if item.attack > 0:
                print('Attack: +{}'.format(item.attack))
            if item.armour > 0:
                print('Armour: +{}'.format(item.armour))
            print('Value: {} coins'.format(item.value))
            if item.heal > 0:
                print('Heal: {} HP'.format(item.heal))
            print('\n')
        continueScreen()
        return
