import BackEnd.Board

if __name__ == "__main__":
    chess_board = BackEnd.Board.board()
    chess_board.display()
    # chess_board.movePiece('12', '44')
    # chess_board.movePiece('11', '46')
    chess_board.movePiece('01', '35')
    chess_board.movePiece('35', '44')
    
    
