class Puzzle:
    def __init__(self, matrix_str = '123456780'):
        self.m = [[int(i) for i in matrix_str[:3]], [int(i) for i in matrix_str[3:6]], [int(i) for i in matrix_str[6:]]]
        self.moves = []
    
    def search(self, n):
        for i in range(self.h + 1):
            for j in range(self.w + 1):
                if self.m[i][j] == n:
                    return i, j

    def move0(self, direction, zero = None):
        zero = self.search(0) if not zero else zero
        to_coord = calc(zero, '+', direction)
        self.m[zero[0]][zero[1]] = self.m[to_coord[0]][to_coord[1]]
        self.m[to_coord[0]][to_coord[1]] = 0
        self.moves.append(direction)


def calc(a, op, b):
    all_calcs = {
        '+': ('a[0] + b[0]', 'a[1] + b[1]'), 
        '-': ('a[0] - b[0]', 'a[1] - b[1]'), 
        '*': ('a[0] * b', 'a[1] * b'), 
        '/': ('a[0] / b', 'a[1] / b')
        }
    return tuple(map(eval, all_calcs[op]))


MOVE_TRANSLATE = {
    (0, 1): 'RIGHT',
    (1, 0): 'DOWN',
    (0, -1): 'LEFT',
    (-1, 0): 'UP'
    }

POSITION_TRANSLATE = ('  ', 'TL', 'TC', 'TR', 'ML', 'MC', 'MR', 'BL', 'BC')

Puzzle(input('\033[1m\nEnter your numbers here: \033[0m')).solve()
