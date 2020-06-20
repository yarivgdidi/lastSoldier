CONST_DEPTH=1

class Board:
    def __init__(self):
        self.boards = {}

############################# This is where magic happens #############################
    def solve(self, board, path):
        for line in range(5):
            for column in range(line + 1):
                for move in ['r', 'dr',  'dl', 'l', 'ul', 'ur' ]:
                    b = self.copyBoard(board['board'])
                    play = 'self.' + move + '( b, ' + str(line) + ',' + str(column) + ')'
                    count = eval(play)
                    if count:
                        key = str(line) + ' - ' + str(column) + ' > ' + move
                        board[key] = {'board': b}
                        if count == CONST_DEPTH:
                           self.success(path + ',' + key)

        for key in board.keys():
            if key != 'board':
                self.solve(board[key], path + ',' + key )
####################################################################################

    def success(self, path):
        self.printPath(path)
        solution = []
        self.getSolutionBoards(self.boards, path, solution)
        self.printBoards(solution)
        print();
        print();


    def printPath(self, path):
        for p in path.split(',')[1:]:
            print(p, end='')
            for i in range(15 - len(p)):
                print(' ', end='')
        print('')


    def createBoard(self):
       return [[1, -1, -1, -1, -1], [1, 1, -1, -1, -1], [1, 1, 1, -1, -1], [1, 1, 1, 1, -1], [1, 1, 1, 1, 1] ]

    def copyBoard(self, board):
        b=self.createBoard()
        for i in range(5):
           for j in range(i+1):
               b[i][j] = board[i][j]
        return b

    def getSolutionBoards(self, board, path, temp):
        first = path.split(',')[0]
        rest = ','.join(path.split(',')[1:])
        if first and rest:
            temp.append(board[first]['board'])
            self.getSolutionBoards(board[first], rest , temp )

    def printBoards(self, boards):
        for i in range(5):
            for b in boards:
                for s in range(4 - i):
                    print(' ', end="")
                for j in range(i + 1):
                    if b[i][j] >= 0:
                        print(b[i][j], " ", end="")
                for s in range(4 - i):
                    print(' ', end="")
                for s in range(4 - i):
                    print(' ', end="")
            print('')

    def printBoard(self, board):
        for i in range(5):
            for s in range(4-i):
                print(' ', end="")
            for j in range( i + 1):
                if board[i][j]>=0:
                    print(board[i][j], " " , end="")
            print('')
        print('')

    def r(self, b, i, j):
        i_ = i
        i__ = i
        j_ = j + 1
        j__ = j +2
        if j__ < 5:
            if  b[i][j] == 1 and b[i_][j_] == 1 and b[i__][j__] == 0:
                b[i][j] = 0
                b[i_][j_] = 0
                b[i__][j__] = 1
                return self.countBoard(b)
        return False

    def l(self, b, i, j):
        i_ = i
        i__ = i
        j_ = j - 1
        j__ = j - 2
        if j__ > 0:
            if  b[i][j] == 1 and b[i_][j_] == 1 and b[i__][j__] == 0:
                b[i][j] = 0
                b[i_][j_] = 0
                b[i__][j__] = 1
                return self.countBoard(b)
        return False

    def dl(self, b, i, j):
        i_ = i + 1
        i__ = i + 2
        j_ = j
        j__ = j
        if i__ < 5:
            if  b[i][j] == 1 and b[i_][j_] == 1 and b[i__][j__] == 0:
                b[i][j] = 0
                b[i_][j_] = 0
                b[i__][j__] = 1
                return self.countBoard(b)
        return False

    def dr(self, b, i, j):
        i_ = i + 1
        i__ = i + 2
        j_ = j + 1
        j__ = j + 2
        if i__ < 5 and j__ < 5:
            if  b[i][j] == 1 and b[i_][j_] == 1 and b[i__][j__] == 0:
                b[i][j] = 0
                b[i_][j_] = 0
                b[i__][j__] = 1
                return self.countBoard(b)
        return False

    def ur(self, b, i, j):
        i_ = i - 1
        i__ = i - 2
        j_ = j
        j__ = j
        if i__ >= 0:
            if  b[i][j] == 1 and b[i_][j_] == 1 and b[i__][j__] == 0:
                b[i][j] = 0
                b[i_][j_] = 0
                b[i__][j__] = 1
                return self.countBoard(b)
        return False

    def ul(self,b, i, j):
        i_ = i - 1
        i__ = i - 2
        j_ = j - 1
        j__ = j - 2
        if i__ >= 0 and j__ >= 0:
            if  b[i][j] == 1 and b[i_][j_] == 1 and b[i__][j__] == 0:
                b[i][j] = 0
                b[i_][j_] = 0
                b[i__][j__] = 1
                return self.countBoard(b)
        return False


    def countBoard(self, board):
        c=0
        for i in range(5):
            for j in range(i+1):
                if board[i][j]==1:
                    c+=1
        return c


    def test(self):

        b=self.createBoard()
        b[4][2] = 0
        self.printBoard(b)
        print("=== right ===")
        self.r(b,4,0)
        self.printBoard( b )
        print ("=== dl ====")
        self.dl(b, 2,1)
        self.printBoard(b)
        print("=== left ====")
        self.l(b, 3,3)
        self.printBoard(b)
        print("=== ur ====")
        self.ur(b, 4, 1)
        self.printBoard(b)
        print("=== dr ====")
        self.dr(b, 1, 0)
        self.printBoard(b)
        print("=== ul ====")
        self.ul(b, 4, 3)
        self.printBoard(b)

board = Board()
#board.test()
board.boards['Start'] = {
    'board': board.createBoard()
}
board.boards['Start']['board'][2][1]=0
board.solve(board.boards['Start'], 'Start')
