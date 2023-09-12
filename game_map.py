import pygame
from pygame.locals import *


def get_font(size):  #Create font style
    return pygame.font.Font("assets/font.ttf", size)

class Game_Map:
    def __init__(self, screen, screen_rect, fps, resolution):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.clock = pygame.time.Clock()

    def game_map(self):
        #Load background
        background = pygame.image.load('assets/Map_BG.png').convert()

        while True:
            #Set fps
            self.clock.tick(self.fps)
            #create background
            self.screen.blit(background, (0,0))

            #Events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            pygame.display.flip()