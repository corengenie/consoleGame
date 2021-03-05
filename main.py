from player import Player
from levelMap import LevelMap
from usable import clear


if __name__ == '__main__':
    myMap = LevelMap(9, 9, 1, 1)
    i = input()
    while i != 'exit':
        clear()
        myMap.move(i)
        myMap.print()
        i = input()
