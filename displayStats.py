from clearScreen import clearScreen
from continueScreen import continueScreen


def displayStats(character):
    clearScreen()
    print('--- Stats of {} ---'.format(character.name))
    print('Health: {}'.format(character.health))
    print('Attack: {}'.format(character.attack))
    print('Defence: {}'.format(character.defence))
    print('Gold: {}'.format(character.gold))
    print('\n')
    continueScreen()
    return
