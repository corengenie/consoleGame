# def matrix_print(arr, n, m):
#     for i in range(n):
#         for j in range(m):
#             print(arr[i][j], end=' ')
#         print()
# def insert(mas1, mas2, w, h, x, y):
#     # mas1 - куда записывать
#     # mas2 - что записывать
#     # w1 - ширина mas2
#     # h - высота mas2
#     # x, y - откуда начинать
#     for i in range(h):
#         for j in range(w):
#             mas1[y+i][x+j] = mas2[i][j]
#     return mas1
# mas = []
# for i in range(5):
#     mas.append([])
#     for j in range(5):
#         mas[i].append('0')
#
# matrix_print(mas, 5, 5)
#
# mas1 = []
# for i in range(2):
#     mas1.append([])
#     for j in range(2):
#         mas1[i].append('2')
#
# matrix_print(mas1, 2, 2)
#
# insert(mas, mas1, 2, 2, 3, 2)
#
# matrix_print(mas, 5, 5)

import os
import rich


def clear(): os.system('cls')


class LevelMap:
    map_array = []
    playerY = None
    playerX = None

    def __init__(self, width, height, startX, startY):
        __a = []
        __a.append('#')
        for i in range(width): __a.append('-')
        __a.append('#')
        self.map_array.append(__a)
        __a = []
        for i in range(1, height):
            __a.append('#')
            for i in range(width): __a.append(' ')
            __a.append('#')
            self.map_array.append(__a)
            __a = []
        __a.append('#')
        for i in range(width): __a.append('-')
        __a.append('#')
        self.map_array.append(__a)
        del(__a)
        # self.map_array[0].append(['#'])
        # self.map_array[0].append(['-' for i in range(width)])
        # self.map_array[0].append(['#'])

        self.playerY = startY
        self.playerX = startX
        self.placeobj(self.playerX, self.playerY, 'O')

    def placeobj(self, x, y, obj):
        self.map_array[y][x] = obj

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


myMap = LevelMap(9, 9, 1, 1)

i = input()
while i != 'exit':
    clear()
    myMap.move(i)
    myMap.print()
    i = input()
