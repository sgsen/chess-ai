import pygame
from const import *

class Dragger:
    def __init__(self):
       self.mouseX = 0
       self.mouseY = 0
       self.initial_row = 0
       self.initial_col = 0
       self.piece = None
       self.dragging = False

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos
        clicked_row = self.mouseY // SQSIZE
        clicked_col = self.mouseX // SQSIZE
        return clicked_row, clicked_col
    
    def save_initial(self, clicked_row, clicked_col):
        self.initial_row = clicked_row
        self.initial_col = clicked_col
        
    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True


    def undrag_piece(self):
        self.piece = None
        self.dragging = False

    def update_blit(self, surface):
        # texture or image file
        self.piece.set_texture(size=128)
    
        # show image
        img = pygame.image.load(self.piece.texture)
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        surface.blit(img, self.piece.texture_rect)
