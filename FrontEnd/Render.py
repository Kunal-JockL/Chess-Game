import pygame
import os

class render:

    WIDTH, HEIGHT = 700, 700
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    squareDimension = (HEIGHT/8, HEIGHT/8)
    colors = ((0, 0, 0), (255, 255, 255))
    squareWidth = WIDTH/8

    FPS = 60

    def main(self):
        
        run = True
        
        while run:
            clock = pygame.time.Clock()
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
            self.renderBoard()
            # self.getMove()
            # self.calcPos(400, 350)
            
            pygame.display.update() 
                    
        pygame.quit()
        
        
    def renderBoard(self):
        for i in range(0,8):
            for j in range(0,8):
                pygame.draw.rect(self.WINDOW , (255, 255, 255) if (i + j) %2 == 0 else (0, 0, 0), pygame.Rect(self.squareWidth * i, self.squareWidth*j, self.squareWidth, self.squareWidth))
        # pygame.draw.rect(self.WINDOW , (0, 0, 255), pygame.Rect(400, 350, self.squareWidth / 5, self.squareWidth/ 5))



    def getMove(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.event.button == 1:
                x , y = self.calcpos(pygame.mouse.get_pos())
                
                
    def calcPos(self, x , y ):
        x = (x // self.squareWidth) * self.squareWidth
        y = (y // self.squareWidth) * self.squareWidth
        return x, y
    
    def highlight(self, x, y):
            highlighter = pygame.transform.scale(pygame.image.load())
    
        
        


if __name__ == "__main__":
    render1 = render()
    render1.main()
