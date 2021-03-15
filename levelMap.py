import random


class LevelMap:
    map_array = []
    playerY = None
    playerX = None
    width, height = None, None
    wall_sign = '*'

    def __init__(self, width, height, startX, startY):
        self.width = width
        self.height = height
        __a = []
        for i in range(width + 2): __a.append('#')
        self.map_array.append(__a)
        __a = []
        for i in range(height):
            __a.append('#')
            for i in range(width): __a.append(' ')
            __a.append('#')
            self.map_array.append(__a)
            __a = []
        for i in range(width + 2): __a.append('#')
        self.map_array.append(__a)
        del(__a)

        self.generator()

        self.playerY = startY
        self.playerX = startX
        self.placeobj(self.playerX, self.playerY, 'O')

    def generator(self):
        for i in range(self.width * 2):
            self.placeobj(random.randint(1, self.width), random.randint(1, self.height - 1), '*')

    # def validator(self):
    #     for i in range(1, self.width - 1):
    #         for j in range(1, self.height - 1):
    #             walls = []
    #             if self.map_array[i][j] == ' ':




    def placeobj(self, x, y, obj):
        self.map_array[y][x] = obj

    def clear(self):
        for i in range(1, self.height):
            for j in range(1, self.height):
                self.placeobj(i, j, ' ')

    def print(self):
        for line in self.map_array:
            for el in line:
                print(el, end=' ')
            print()

    def move(self, direction):
        if direction in ('w', 'up'):
            if self.map_array[self.playerY - 1][self.playerX] == ' ':
                self.map_array[self.playerY][self.playerX] = ' '
                self.map_array[self.playerY - 1][self.playerX] = '0'
                self.playerY -= 1
        elif direction in ('s', 'down'):
            if self.map_array[self.playerY + 1][self.playerX] == ' ':
                self.map_array[self.playerY][self.playerX] = ' '
                self.map_array[self.playerY + 1][self.playerX] = '0'
                self.playerY += 1
        elif direction in ('a', 'left'):
            if self.map_array[self.playerY][self.playerX - 1] == ' ':
                self.map_array[self.playerY][self.playerX] = ' '
                self.map_array[self.playerY][self.playerX - 1] = '0'
                self.playerX -= 1
        elif direction in ('d', 'right'):
            if self.map_array[self.playerY][self.playerX + 1] == ' ':
                self.map_array[self.playerY][self.playerX] = ' '
                self.map_array[self.playerY][self.playerX + 1] = '0'
                self.playerX += 1


if __name__ == '__main__':
    mapp = LevelMap(9, 9, 1, 1)
    mapp.print()
    mapp.clear()
    mapp.generator()
    mapp.print()
    mapp.clear()
    mapp.generator()
    mapp.print()
    mapp.clear()
    mapp.generator()
    mapp.print()
    mapp.clear()
