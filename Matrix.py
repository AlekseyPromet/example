import random


class Matrix:

    def __init__(self, row, col):
        self.n = row
        self.matrix = [[random.randrange(0, 10) for a in range(col)] for b in range(row)]

    def print(self):
        matrix = self.matrix
        for im in range(len(matrix)):
            print(matrix[im])

    def find_max(self):
        max_sum = 0
        n = self.n
        m = self.matrix
        index = -1
        for x in range(n):
            if sum(m[x]) > max_sum:
                max_sum = sum(m[x])
                index = x
        print("максимум: %s, индекс: %s" % (max_sum, index))
        return max_sum, index

    def remove_max_row(self):
        m = self.matrix
        n = self.n
        max_value, index = self.find_max()
        m.remove(m[index])
        for im in range(n-1):
            print(m[im])

M1 = Matrix(5, 5)

M1.print()
print('-'*100)
M1.remove_max_row()
