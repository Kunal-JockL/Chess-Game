class board:
    def __init__(self):

        self.board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]

    def display(self):
        for row in self.board:
            print("  ".join(map(self.displayPiece, row))) 

    def displayPiece(self, piece):
        piece_symbols = {
            'K': '♔', 
            'Q': '♕', 
            'R': '♖', 
            'B': '♗', 
            'N': '♘', 
            'P': '♙',
            'k': '♚', 
            'q': '♛', 
            'r': '♜', 
            'b': '♝', 
            'n': '♞', 
            'p': '♟',
            '.': '.'    }
        return piece_symbols.get(piece)
    
    def movePiece(self, start, end):
        start = [int(start[0]), int(start[1])]#error might be here
        end = [int(end[0]), int(end[1])]

        validPos = self.validity(start)
        print(validPos)


        self.board[start[0]][start[1]], self.board[end[0]][end[1]] = self.board[end[0]][end[1]], self.board[start[0]][start[1]]
        self.display()


    def validity(self, pos):
        piece = self.board[pos[0]][pos[1]]

        pieceDict= {
            'K': self.validityKing,
            'Q': self.validityQueen,
            'R': self.validityRook,
            'B': self.validityBishop,
            'N': self.validityKnight,
            'P': self.validityPawnWhite,
            'k': self.validityKing,
            'q': self.validityQueen,
            'r': self.validityRook,
            'b': self.validityBishop,
            'n': self.validityKnight,
            'p': self.validityPawnBlack,
            '.': self.validityNone
        }
        
        return pieceDict.get(piece)(pos)
    
    def validityKing(self, pos):
        row, col = pos[0], pos[1]
        moves = [
            (row-1, col-1), (row-1, col), (row-1, col+1),
            (row, col-1),                 (row, col+1),
            (row+1, col-1), (row+1, col), (row+1, col+1)
        ]
        
        validMoves = [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == '.']

        return validMoves


    def validityQueen(self, pos):
        # Validation logic for queen
        return "Validating queen"

    def validityRook(self, pos):
        row, col = pos[0], pos[1]

        rowMoves, colMoves= [], []
        crossFlag = False

        for i in range(8):
            if self.board[row][i] == '.':
                rowMoves.append((row, i))
            elif (self.board[row][i] == 'r' or self.board[row][i] == 'R') and not crossFlag:
                crossFlag = True
            elif not crossFlag:
                rowMoves = []
            else:
                break
        
        crossFlag = False

        for i in range(8):
            if self.board[i][col] == '.':
                colMoves.append((i, col))
            elif (self.board[i][col] == 'r' or self.board[i][col] == 'R') and not crossFlag:
                crossFlag = True
            elif not crossFlag:
                colMoves = []
            else:
                break

        validMoves = rowMoves + colMoves

        return validMoves

    def validityBishop(self, pos):
        row, col = pos[0], pos[1]

        diffMoves, smMoves= [], []
        crossFlag = False
        
        for i, j in zip(range(min(row+ col, 7), max((row+ col)- 7, 0) - 1, -1) , range(max((row+ col)- 7, 0), min(row+ col, 7) + 1)):
            # print(range(min(row+ col, 7), max((row+ col)- 7, 0) - 1, -1) , range(max((row+ col)- 7, 0), min(row+ col, 7) + 1));
            if self.board[i][j] == '.':
                print(i,j)
                diffMoves.append((i, j))
            elif (self.board[i][j] == 'b' or self.board[i][j] == 'B') and not crossFlag:
                crossFlag = True
            elif not crossFlag:
                diffMoves = []
            else:
                break
        
        crossFlag = False

        for i, j in zip(range(7 if row >= col else row + (7 - col), -1 if row<= col else row - col - 1, -1), range ( 7 if row <= col else col + (7 - row), -1 if row >= col else col - row - 1, -1)):
            # print(range(7 if row >= col else row + (7 - col), -1 if row<= col else row - col - 1, -1), range ( 7 if row <= col else col + (7 - row), -1 if row >= col else col - row - 1, -1))
            if self.board[i][j] == '.':
                smMoves.append((i, j))
            elif (self.board[i][j] == 'b' or self.board[i][j] == 'B') and not crossFlag:
                crossFlag = True
            elif not crossFlag:
                smMoves = []
            else:
                break

        validMoves = diffMoves + smMoves

        return validMoves


    def validityKnight(self, pos):
        row, col = pos[0], pos[1]
        
        onesArray, twosArray = [1, -1],[2, -2]
        
        validMoves = []
        
        for i in range(2):
            for j in range(2):
                if self.board[row + onesArray[ i ]][col + twosArray[ j ]] == '.':
                    # print(row + onesArray[ i ], col + twosArray[ j ])
                    validMoves.append((row + onesArray[ i ], col + twosArray[ j ]))
                if self.board[row + twosArray[ i ]][col + onesArray[ j ]] == '.':
                    # print(row + twosArray[ i ], col + onesArray[ j ])
                    validMoves.append((row + twosArray[ i ], col + onesArray[ j ]))
                    
        return validMoves

    def validityPawnBlack(self, pos):
        # Validation logic for pawn
        return "Validating pawn"
    
    def validityPawnWhite(self, pos):
        # Validation logic for pawn
        return "Validating pawn"
    
    def validityNone(self, pos):

        return "none"

    
    
