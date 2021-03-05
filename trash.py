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

