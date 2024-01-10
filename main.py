from Game import Game

if __name__ == "__main__":
    
    chessGame = Game()
   
    while(chessGame.isRunning):
        chessGame.handleEvents()
        chessGame.update()
        chessGame.render()
    
    chessGame.clean()
    
    # chess_board.movePiece('01', '35')
    # chess_board.movePiece('35', '44')