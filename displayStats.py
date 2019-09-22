from clearScreen import clear_screen
from continueScreen import continue_screen


def display_stats(character):
    clear_screen()
    print('--- Stats of {} ---'.format(character.name))
    print('Health: {}'.format(character.health))
    print('Attack: {}'.format(character.attack))
    print('Defence: {}'.format(character.defence))
    print('Gold: {}'.format(character.gold))
    print('\n')
    continue_screen()
    return
