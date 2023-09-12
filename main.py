import pygame
import config as config
from main_menu import Menu

while True:
    pygame.init()

    #set screen
    screen = pygame.display.set_mode(config.resolution)
    screen_rect = screen.get_rect()

    #set screen name
    pygame.display.set_caption('Death To The Plague')

    main_menu = Menu(screen, screen_rect, config.fps, config.resolution)
    main_menu.main_menu()