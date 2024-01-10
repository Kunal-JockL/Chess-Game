import pygame
import os
import Board
import Render

from Piece import Piece

class Game:
    def __init__(self):
        self.renderer = Render.render()
        self.chess_board = Board.board(self.renderer.WINDOW)
        self.isRunning = True
        
        self.chess_board.display()
        self.renderer.renderBoard()
        
        
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.renderer.getMove()
                            
        #self.chess_board.handleEvents()

    def render(self):
        clock = pygame.time.Clock()
        clock.tick(self.renderer.FPS)
        
        self.chess_board.render()
                            
        # self.renderer.renderPieces(self.chess_board.board)            
        pygame.display.update()

    def update(self):
        a = 10
        #self.chess_board.update()
        
    def clean(self):
        pygame.quit()
        
        