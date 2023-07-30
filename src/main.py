""" 
    importing libraries 
"""
import pygame
import sys

"""
    importing classes    
"""

from const import *
from game import Game
from square import Square
from move import Move

class Main:
    """class Main"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()
        
    
    def mainloop(self):
        
        game = self.game
        screen = self.screen
        dragger = self.game.dragger
        board = self.game.board
         
        while True:
            #show methods
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            
            if(dragger.dragging):
                dragger.update_blit(screen)
            
            for event in pygame.event.get():
                #click event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE 
                    
                    #if clicked square has a piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        # check if it is a valid piece color
                        if piece.color == game.next_player:
                            board.calc_move(piece, clicked_row, clicked_col)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                        
                        # show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        
                #mouse motion 
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        
                        #show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                
                #click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        
                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE
                    
                        #create possible move
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row,released_col)

                        move = Move(initial, final )
                        
                        #checking for valid move
                        if board.valid_move(dragger.piece, move):
                            board.move(dragger.piece, move)
                            
                            #show methods
                            game.show_bg(screen)
                            game.show_pieces(screen)
                            
                            # next turn
                            game.next_turn()
                    
                    dragger.undrag_piece()
                
                
                #quick application
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            
            
                    
            pygame.display.update()
    
main = Main()
main.mainloop()
    