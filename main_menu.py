import pygame, sys
from button import Button
from game_map import Game_Map
from options import Options
from main_menu_background import *


#Load font
def get_font(size):  #Create font style
    return pygame.font.Font("assets/font.ttf", size)

class Menu:
    def __init__(self, screen, screen_rect, fps, resolution):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.clock = pygame.time.Clock()

    def main_menu(self):
        #Objects instances
        game_map = Game_Map(self.screen, self.screen_rect, self.fps, self.resolution)
        options = Options(self.screen, self.screen_rect, self.fps, self.resolution)

        #Load background images
        background_menu = Background_Menu()
        #Font settings
        text_color = "#cdcdcd"
        hover_text_color = "Red"
        overlay = pygame.image.load("assets/Menu_Overlay.png")

        #Title
        title_text = get_font(40).render("Death To The Plague", True, text_color)
        title_rect = title_text.get_rect(center=(self.screen_rect.centerx + 180, self.screen_rect.top+100))

        play_button = Button(image=overlay, pos=(self.screen_rect.centerx+ 180, self.screen_rect.centery-100), text_input="Iniciar",
                            font=get_font(44), base_color=text_color, hovering_color=hover_text_color)
        options_button = Button(image=overlay, pos=(self.screen_rect.centerx + 180, self.screen_rect.centery), text_input="Ajustes",
                            font=get_font(44), base_color=text_color, hovering_color=hover_text_color)
        quit_button = Button(image=overlay, pos=(self.screen_rect.centerx+ 180, self.screen_rect.centery+100), text_input="Sair",
                            font=get_font(44), base_color=text_color, hovering_color=hover_text_color)

        aply_changes_config = False

        while True:
            # set frames
            self.clock.tick(self.fps)

            menu_mouse_position = pygame.mouse.get_pos()

            # draw background
            self.screen.blit(background_menu.image, (0, 0))
            background_menu.update()

            # draw menu text
            self.screen.blit(title_text, title_rect)

            # draw button
            for button in [play_button, options_button, quit_button]:
                button.changeColor(menu_mouse_position)
                button.update(self.screen)

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(menu_mouse_position):
                        #Start game
                        game_map.game_map()
                    if options_button.checkForInput(menu_mouse_position):
                        options.options()
                        aply_changes_config = True
                    if quit_button.checkForInput(menu_mouse_position):
                        pygame.quit()
                        sys.exit()

            if aply_changes_config == True:
                break

            # update
            pygame.display.flip()