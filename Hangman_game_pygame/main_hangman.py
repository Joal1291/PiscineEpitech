import pygame as py
import time
import random
import funct_title_screen as ts


py.init()
py.display.set_caption('Hangman Game')

screen_resolution = (1000, 656)
flags = py.DOUBLEBUF | py.HWSURFACE
screen = py.display.set_mode(screen_resolution, flags)

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
            print(position)
#--------------------------------------------------------------------------------------------------------------------------


#----------------------------------------- Function traveller
def title_screen():
    py.display.set_caption('Hangman Game - Main Menu')
    # game = False
    # record = False
    ts.title_screen_animation(screen)

    button_play_surface = py.image.load("image/image_play.png")
    button_play_surface = py.transform.scale(button_play_surface, (250, 100))

    button_play = Button(button_play_surface, 250, 550)

    button_record_surface = py.image.load("image/image_record.png")
    button_record_surface = py.transform.scale(button_record_surface, (250,140))

    button_record = Button(button_record_surface, 750, 565)

    while True:
        background_surface = py.image.load("image_anim_title_screen/output_image_208.png")
        name_game_surface = py.image.load("image/namegamewhite.png")

        button_play_surface = py.image.load("image/image_play.png")
        button_play_surface = py.transform.scale(button_play_surface, (250, 100))
        button_play = Button(button_play_surface, 250, 550)

        button_record_surface = py.image.load("image/image_record.png")
        button_record_surface = py.transform.scale(button_record_surface, (250,140))
        button_record = Button(button_record_surface, 750, 565)

        button_quit_surface = py.image.load("image/image_quit.png")
        button_quit_surface = py.transform.scale(button_quit_surface, (150, 100))
        button_quit = Button(button_quit_surface, 500, 600)
        
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.MOUSEBUTTONDOWN:
                button_play.check_position_input(py.mouse.get_pos())
                button_record.check_position_input(py.mouse.get_pos())
                button_quit.check_position_input(py.mouse.get_pos())

        screen.blit(background_surface, (0, 0))
        screen.blit(name_game_surface, (250, 200))
        button_play.update()
        button_record.update()
        button_quit.update()
        py.display.update()
        py.display.flip()

title_screen()
#-----------------------------------------------------------------------------------------
