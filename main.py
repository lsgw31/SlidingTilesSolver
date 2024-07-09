import random
class Puzzle:
    def __init__(self, matrix_str = '12345678'):
        matrix_str += '0'
        self.m = [[int(i) for i in matrix_str[:3]], [int(i) for i in matrix_str[3:6]], [int(i) for i in matrix_str[6:]]]
        self.moves = []
    
    def search(self, n = 0):
        for i in range(3):
            for j in range(3):
                if self.m[i][j] == n:
                    return i, j

    def move0(self, direction, zero = None):
        zero = self.search(0) if not zero else zero
        to_coord = calc(zero, '+', direction)
        self.m[zero[0]][zero[1]] = self.m[to_coord[0]][to_coord[1]]
        self.m[to_coord[0]][to_coord[1]] = 0
        self.moves.append(direction)
    
    def solve(self):
        print('\nIf you entered your numbers correctly, this is what your puzzle should look like:')
        print('\033[1m' + '\n'.join(' '.join(str(j) if j else ' ' for j in i) for i in self.m) + '\033[0m')

        self.place1()
        self.print_moves_and_puzzle()

        # # First set of 2 (2 & 3)
        # self.print_moves_and_puzzle()

        # # Second set of 2 (4 & 7) (Share a method with above?)
        # self.print_moves_and_puzzle()

        # # Rotate BL 2x2 till it's solved
        # self.print_moves_and_puzzle(solved = True)
    
    def print_moves_and_puzzle(self, *, solved = False):
        # for i in range(1, random.randint(5, 20)):
        #     self.moves.append(random.choice(tuple(MOVE_TRANSLATE.keys())))  # for testing so that it can make moves and dev can see UI

        print('\n\nNow make these moves:')
        print(', '.join(MOVE_TRANSLATE[i] for i in self.moves))
        self.moves.clear()
        if not solved:
            print('\nYour puzzle should now look like this:')
            print('\033[1m' + '\n'.join(' '.join(str(j) if j else ' ' for j in i) for i in self.m) + '\033[0m')
        else:
            print('\n\033[1mYour puzzle should now be solved!\033[0m')
    
    def rotate2x2(self, coord, direction):
        d = len(direction) - 1
        for i in range(4):
            self.move0(ALL_2X2_ROTATIONS[coord][d][i], LOCATIONS_IN_ROTATIONS[coord][-d - (2 * d - 1) * i])
    
    def place1(self):
        if self.m[2][1] == 1:  # put 0 in center; avoid putting 1 in BR
            self.move0((-1, 0), (2, 2))
            self.move0((0, -1), (1, 2))
        else:
            self.move0((0, -1), (2, 2))
            self.move0((-1, 0), (2, 1))
        
        one = self.search(1)
        if one in ((0, 1), (0, 2), (1, 2)):
            direction = 'c'
        else:
            direction = 'cc'
        
        for sub_coord in ONE_ROTATIONS[direction][3 - one[0] - one[1]:]:
            self.rotate2x2(sub_coord, direction)
        
        

def calc(a, op, b):
    return tuple(map(eval, ALL_CALCS[op]))


MOVE_TRANSLATE = {
    (0, 1): 'RIGHT',
    (1, 0): 'DOWN',
    (0, -1): 'LEFT',
    (-1, 0): 'UP'
    }

ALL_CALCS = {
    '+': ('a[0] + b[0]', 'a[1] + b[1]'), 
    '-': ('a[0] - b[0]', 'a[1] - b[1]'), 
    '*': ('a[0] * b', 'a[1] * b'), 
    '/': ('a[0] / b', 'a[1] / b')
    }

ALL_2X2_ROTATIONS = {
    (0, 0): (((0, -1), (-1, 0), (0, 1), (1, 0)), 
             ((-1, 0), (0, -1), (1, 0), (0, 1))),

    (0, 1): (((-1, 0), (0, 1), (1, 0), (0, -1)), 
             ((0, 1), (-1, 0), (0, -1), (1, 0))),

    (1, 0): (((1, 0), (0, -1), (-1, 0), (0, 1)), 
             ((0, -1), (1, 0), (0, 1), (-1, 0))),

    (1, 1): (((0, 1), (1, 0), (0, -1), (-1, 0)), 
             ((1, 0), (0, 1), (-1, 0), (0, -1)))
}

LOCATIONS_IN_ROTATIONS = {
    (0, 0): ((1, 1), (1, 0), (0, 0), (0, 1), (1, 1)), 
    
    (0, 1): ((1, 1), (0, 1), (0, 2), (1, 2), (1, 1)), 
    
    (1, 0): ((1, 1), (2, 1), (2, 0), (1, 0), (1, 1)), 
    
    (1, 1): ((1, 1), (1, 2), (2, 2), (2, 1), (1, 1))
}


ONE_ROTATIONS = {
    'c': ((0, 1), (0, 1), (0, 0)),

    'cc': ((1, 0), (1, 0), (0, 0))
}

Puzzle(input('\033[1m\nEnter your numbers here: \033[0m')).solve()
