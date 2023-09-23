import pygame, sys
import time
import random
import funct_title_screen as ts


pygame.init()
pygame.display.set_caption('Hangman Game')

screen_resolution = (1000, 656)
flags = pygame.DOUBLEBUF | pygame.HWSURFACE |pygame.NOFRAME
screen = pygame.display.set_mode(screen_resolution, flags)

#----------------------------------------- CLASS
class Button():
    def __init__(self, image, x_pos, y_pos):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self):
        screen.blit(self.image, self.rect)
    
    def check_position_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        else:
            return False
#--------------------------------------------------------------------------------------------------------------------------

#----------------------------------------- Record Page
def record_page():

    while True:
        mouse_position = pygame.mouse.get_pos()

        background_surface = pygame.image.load("image_anim_title_screen/output_image_18.png")

        record_title_page_image = pygame.image.load("image/record_page_titlte.png")

        button_back_image = pygame.image.load("image/image_back.png")
        button_back_image = pygame.transform.scale(button_back_image, (250,100))
        button_back = Button(button_back_image, 850, 600)
        
        screen.blit(background_surface, (0, 0))
        button_back.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.check_position_input(mouse_position):
                    title_screen(1)

        pygame.display.update()

#---------------------------------------------------------------------------------------------------------------------------
#----------------------------------------- Play Page
def play_page():

    while True:
        mouse_position = pygame.mouse.get_pos()

        background_surface = pygame.image.load("image_anim_title_screen/output_image_160.png")

        button_back_image = pygame.image.load("image/image_back.png")
        button_back_image = pygame.transform.scale(button_back_image, (250,100))
        button_back = Button(button_back_image, 850, 600)
        
        screen.blit(background_surface, (0, 0))
        button_back.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.check_position_input(mouse_position):
                    title_screen(1)

        pygame.display.update()

#---------------------------------------------------------------------------------------------------------------------------
#----------------------------------------- Function traveller
def title_screen(x):
    pygame.display.set_caption('Hangman Game - Main Menu')
    # game = False
    # record = False
    if x == 0:
        ts.title_screen_animation(screen)

    while True:
        mouse_position = pygame.mouse.get_pos()

        background_surface = pygame.image.load("image_anim_title_screen/output_image_208.png")
        name_game_surface = pygame.image.load("image/namegamewhite.png")

        button_play_surface = pygame.image.load("image/image_play.png")
        button_play_surface = pygame.transform.scale(button_play_surface, (250, 100))
        button_play = Button(button_play_surface, 250, 550)

        button_record_surface = pygame.image.load("image/image_record.png")
        button_record_surface = pygame.transform.scale(button_record_surface, (250,140))
        button_record = Button(button_record_surface, 750, 565)

        button_quit_surface = pygame.image.load("image/image_quit.png")
        button_quit_surface = pygame.transform.scale(button_quit_surface, (150, 100))
        button_quit = Button(button_quit_surface, 500, 600)
        
        # screen.blit(background_surface, (0, 0))
        # screen.blit(name_game_surface, (250, 200))
        # button_play.update()
        # button_record.update()
        # button_quit.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_record.check_position_input(mouse_position):
                    record_page()
                if button_quit.check_position_input(mouse_position):
                    pygame.quit()
                    sys.exit()
                if button_play.check_position_input(mouse_position):
                    play_page()

        screen.blit(background_surface, (0, 0))
        screen.blit(name_game_surface, (250, 200))
        button_play.update()
        button_record.update()
        button_quit.update()
        pygame.display.update()
        # pygame.display.flip()

title_screen(0)
#-----------------------------------------------------------------------------------------
