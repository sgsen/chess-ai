import pygame
import sys  
from const import *

from game import Game

class Main:
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
            game.show_bg(screen)
            game.show_pieces(screen)
            
            # show dragging piece
            if dragger.dragging:
                dragger.update_blit(screen)
            
            for event in pygame.event.get():
                # mouse click on piece
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_row, clicked_col = dragger.update_mouse(event.pos)

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(clicked_row, clicked_col)
                        dragger.drag_piece(piece)
 
                    else:
                        piece = None
                    
                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        dragger.update_blit(screen)

                # mouse release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                # quit
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            
            pygame.display.update()

main = Main()
main.mainloop()
