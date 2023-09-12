import pygame

class Background_Menu():
    def __init__(self):
        #Sprites
        self.sprites = [pygame.image.load('assets/Menu_Background/Main_Menu_BG1.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG2.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG3.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG4.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG5.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG6.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG7.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG8.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG9.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG10.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG11.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG12.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG13.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG14.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG15.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG16.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG17.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG18.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG19.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG20.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG21.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG22.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG23.png'),
                        pygame.image.load('assets/Menu_Background/Main_Menu_BG24.png')]
        self.image = self.sprites[0]
        self.current_sprite = 0

    def update(self):
        #Animation controll
        self.current_sprite = self.current_sprite + 0.08
        if self.current_sprite > 23:
            self.current_sprite = 0

        #Current Image
        self.image = self.sprites[int(self.current_sprite)]
