import pygame, sys
import config as config
from button import Button
from main_menu_background import *


# Load font
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

class Options:
    def __init__(self, screen, screen_rect, fps, resolution):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.clock = pygame.time.Clock()

    def options(self):
        # background image
        background_menu = Background_Menu()

        #Button settings
        text_color = "#cdcdcd"
        hover_text_color = "Red"
        overlay = pygame.image.load("assets/Menu_Overlay.png")

        #Buttons display
        fps_button = Button(image=overlay, pos=(self.screen_rect.centerx, self.screen_rect.centery), text_input=f"{config.fps}",
                            font=get_font(44), base_color=text_color, hovering_color=hover_text_color)
        apply_button = Button(image=overlay, pos=(self.screen_rect.centerx, self.screen_rect.top + 300), text_input="Aplicar",
                            font=get_font(44), base_color=text_color, hovering_color=hover_text_color)

        #Display validator
        back_to_menu = False

        while True:
            #Set fps
            self.clock.tick(self.fps)

            #Mouse position
            option_mouse_position = pygame.mouse.get_pos()

            #create background
            self.screen.blit(background_menu.image, (0,0))
            background_menu.update()

            #create button
            for button in [fps_button, apply_button]:
                button.changeColor(option_mouse_position)
                button.update(self.screen)

            #event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #Validator configs
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if fps_button.checkForInput(option_mouse_position):
                        if config.fps == 30:
                            config.fps = 60
                        else:
                            config.fps = 30

                    fps_button = Button(image=overlay, pos=(self.screen_rect.centerx,self.screen_rect.centery), text_input=f"{config.fps}",
                                        font=get_font(44), base_color=text_color, hovering_color=hover_text_color)

                    if apply_button.checkForInput(option_mouse_position):
                        back_to_menu = True

            if back_to_menu == True:
                break

            #Update
            pygame.display.flip()
