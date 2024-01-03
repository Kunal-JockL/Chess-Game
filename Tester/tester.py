if __name__ == "__main__":
    
    board = [
            ['R', 'N', '.', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'B', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
    
    row = 3
    col = 4
    
    print('ttt')
    
    diffMoves = []
    crossFlag = False
    
    print(min(row+ col, 7), max((row+ col)- 7, 0),max((row+ col)- 7, 0), min(row+ col, 7))
    for i, j in zip(range(min(row+ col, 7), max((row+ col)- 7, 0), -1), range(max((row+ col)- 7, 0), min(row+ col, 7))):
            print("In")
            if board[i][j] == '.':
                diffMoves.append((i, j))
                print('1')
            elif (board[i][j] == 'b' or board[i][j] == 'B') and not crossFlag:
                crossFlag = True
                print('2')
            elif not crossFlag:
                diffMoves = []
                print('3')
            else:
                print('4')
                break