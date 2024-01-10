import pygame
import os

pygame.init()

class coordinate:
    def __init__(self):
        self.x = 0
        self.y = 0

class render:

    WIDTH, HEIGHT = 800, 800
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    colors = ((0, 0, 0), (255, 255, 255))
    squareWidth = WIDTH/8
    pieceDimension = (squareWidth/10) * 8


    FPS = 60

    def main(self):
        
        run = True
        
        self.renderBoard()
        
        while run:
            clock = pygame.time.Clock()
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.getMove()
                        
            self.renderpieces()            
            pygame.display.update() 
                    
        pygame.quit()
        
        
    def renderBoard(self):
        for i in range(0,8):
            for j in range(0,8):
                pygame.draw.rect(self.WINDOW , (255, 210, 140) if (i + j) %2 == 0 else (255, 160, 90), pygame.Rect(self.squareWidth * i, self.squareWidth*j, self.squareWidth, self.squareWidth))
        # pygame.draw.rect(self.WINDOW , (0, 0, 255), pygame.Rect(400, 350, self.squareWidth / 5, self.squareWidth/ 5))



    def getMove(self):
        point = coordinate()
        point.x, point.y =pygame.mouse.get_pos()
        self.calcPos(self.calcIndex(point))
        
                

    def calcIndex(self, point):
        point.x = point.x // self.squareWidth
        point.y = point.y // self.squareWidth
        return point
    
    def calcPos(self, point):
        point.x =  point.x * self.squareWidth
        point.y =  point.y * self.squareWidth
        self.highlight(point)
    
    def highlight(self, point):
        highlighterImagePath = os.path.normpath(os.path.join(os.getcwd(), 'assets/highlighter.png'))
        highlighter = pygame.transform.scale(pygame.image.load(highlighterImagePath).convert_alpha(), (self.squareWidth, self.squareWidth))
        for _ in range(3):
            self.WINDOW.blit(highlighter, (point.x, point.y))
    
        
    def renderPieces(self, board):
        for row in range(8):
            for col in range(8):
                point = coordinate()
                point.x , point.y = row, col
                self.renderPieceSelector(board[row][col], point)
                print(point)
                # print(board[row][col])
                
    def renderPieceSelector(self , pieceSymbol, point):        
        if pieceSymbol == '.':
            return
        
        pieceDict= {
            'K': 'assets/whiteKing.png',
            'Q': 'assets/whiteQueen.png',
            'R': 'assets/whiteRook.png',
            'B': 'assets/whiteBishop.png',
            'N': 'assets/whiteKnight.png',
            'P': 'assets/whitePawn.png',
            'k': 'assets/blackKing.png',
            'q': 'assets/blackQueen.png',
            'r': 'assets/blackRook.png',
            'b': 'assets/blackBishop.png',
            'n': 'assets/blackKnight.png',
            'p': 'assets/blackPawn.png'       
        }
        
        imagePath = os.path.normpath(os.path.join(os.getcwd(), pieceDict.get(pieceSymbol)))
        image = pygame.transform.scale(pygame.image.load(imagePath).convert_alpha(), (self.pieceDimension, self.pieceDimension))
        self.calcPos(point)
        self.WINDOW.blit(image , (point.x, point.y))
        

if __name__ == "__main__":
    render1 = render()
    render1.main()
