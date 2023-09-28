import pygame, sys
import time
import random
import funct_title_screen as ts


pygame.init()
pygame.display.set_caption('Hangman Game')

screen_resolution = (1000, 656)
flags = pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME 
screen = pygame.display.set_mode(screen_resolution, flags)

#---------------------------------------- LIST and DICTS
list_of_word_to_display:list = ['bouilloire', 'discussions', 'intelligent', 'dentifrice', 'microscope', 'japonais', 'cartographie', 'radiation', 'ensorceler', 'taverne', 'cachette', 'chameau', 'flotteur', 'cascade', 'flotteur', 'diligence', 'prononcer', 'vignoble', 'substitution', 'puissance', 'hieroglyphe', 'principal', 'mitrailleuse', 'prisme', 'impulsion', 'violet', 'partenariat', 'digestion', 'photocopie', 'diplomate', 'agitateur', 'himalaya', 'insensible', 'restaurant', 'cosmetique', 'tropique', 'sonnaille', 'muletier', 'bouteille', 'frauduleux', 'armure', 'crasseux', 'obelisque', 'applaudir', 'inspecter', 'marathon', 'sensible', 'commencer', 'visage', 'entacher', 'cicatrice', 'remarques', 'ombre', 'clairon', 'mathematiques', 'ventiler', 'indivisible', 'alarme', 'mouvements', 'martien', 'symphonie', 'lobotomie', 'dauphins', 'objectif', 'gauche', 'droite', 'tromperie', 'quantum', 'condamner', 'abrasif', 'susciter', 'rebelle', 'chaussures', 'trousse', 'princesse', 'glissant', 'nicotine', 'cannelle', 'chemisier', 'melanger', 'chinois', 'horreurs', 'marches', 'humilite', 'tentacule', 'trombone', 'banque', 'carburant', 'annonce', 'viande', 'transport', 'cure-dents', 'avocat', 'couches', 'instruit', 'sondage', 'trolleybus', 'interdimensionnel', 'crocodile', 'holocauste']
imageletterdict:dict = {'a': pygame.image.load("image/image_letter/image_letter_a.png"), 'b': pygame.image.load("image/image_letter/image_letter_b.png"), 'c': pygame.image.load("image/image_letter/image_letter_c.png"), 'd': pygame.image.load("image/image_letter/image_letter_d.png"), 'e': pygame.image.load("image/image_letter/image_letter_e.png"), 'f': pygame.image.load("image/image_letter/image_letter_f.png"), 'g': pygame.image.load("image/image_letter/image_letter_g.png"), 'h': pygame.image.load("image/image_letter/image_letter_h.png"), 'i': pygame.image.load("image/image_letter/image_letter_i.png"), 'j':pygame.image.load("image/image_letter/image_letter_j.png"), 'k': pygame.image.load("image/image_letter/image_letter_k.png"), 'l': pygame.image.load("image/image_letter/image_letter_l.png"), 'm': pygame.image.load("image/image_letter/image_letter_m.png"), 'n': pygame.image.load("image/image_letter/image_letter_n.png"), 'o': pygame.image.load("image/image_letter/image_letter_o.png"), 'p': pygame.image.load("image/image_letter/image_letter_p.png"), 'q': pygame.image.load("image/image_letter/image_letter_q.png"), 'r': pygame.image.load("image/image_letter/image_letter_r.png"), 's': pygame.image.load("image/image_letter/image_letter_s.png"), 't': pygame.image.load("image/image_letter/image_letter_t.png"), 'u': pygame.image.load("image/image_letter/image_letter_u.png"), 'v': pygame.image.load("image/image_letter/image_letter_v.png"), 'w': pygame.image.load("image/image_letter/image_letter_w.png"), 'x': pygame.image.load("image/image_letter/image_letter_x.png"), 'y': pygame.image.load("image/image_letter/image_letter_y.png"), 'z': pygame.image.load("image/image_letter/image_letter_z.png"), '_': pygame.image.load("./image/image_underscore.png")}
#--------------------------------------------------------------------------------------------------------------------------
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
#----------------------------------------- Function
def createButton(letter, x_pos, y_pos):
    button = pygame.image.load(f"image/image_letter/image_letter_{letter}.png")
    button = pygame.transform.scale(button, (70, 70))
    final_button = Button(button, x_pos, y_pos)
    return final_button
def checkletter(letter, word, letterlist, displaygame, display, chance):
    if letter in letterlist:
        print("already played that letter")
    elif letter in word:
        print("the letter is in the world")
        letterlist.insert(0, letter)
        index = [i for i, c in enumerate(word)if c == letter]
        for i in index:
            displaygame = ""
            position:int = i
            display = display[:position] + letter + display[position+1:]
            for i in display:
                displaygame += i + ""
                print(displaygame)
                return displaygame
    elif letter not in word:
        letterlist.insert(0, letter)
        chance += -1
        print(letter, letterlist)
def displayingame(display_in_game):
    position_x = 200
    for i in display_in_game:
            screen.blit(imageletterdict[i], (position_x, 340))
            position_x += 60 
        
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
        screen.blit(record_title_page_image, (300, 0))
        button_back.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.check_position_input(mouse_position):
                    title_screen(1)

        pygame.display.update()

#---------------------------------------------------------------------------------------------------------------------------
#----------------------------------------- Play Page
def play_page(a, b):
    list_of_used_letter:list = []

    nbr_game_played = a
    nbr_point = b
    nbr_chance = 5
    mistery_word = list_of_word_to_display[random.randint(0, len(list_of_word_to_display))]
    displayundescored = "_"*len(mistery_word)
    display = "".join(displayundescored)
    display_in_game = "".join(display)

    while True:

        # letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        mouse_position = pygame.mouse.get_pos()

        #---Style
        background_surface = pygame.image.load("image_anim_title_screen/output_image_160.png")
        fight_surface = pygame.image.load("image/fight_surface.png")
        score_surface = pygame.image.load("image/image_score.png")
        score_surface = pygame.transform.scale(score_surface, (150, 100))
        volcano_surface = pygame.image.load("image/image _volcano.png")

        #---Back button
        button_back_image = pygame.image.load("image/image_back.png")
        button_back_image = pygame.transform.scale(button_back_image, (250,100))
        button_back = Button(button_back_image, 850, 600)
        #---Guess button
        button_guess_image = pygame.image.load("image/image_guess.png")
        button_guess_image = pygame.transform.scale(button_guess_image, (150, 100))
        button_guess = Button(button_guess_image, 580, 550)
        
        screen.blit(background_surface, (0, 0))
        screen.blit(volcano_surface, (-50, -50))
        screen.blit(fight_surface, (-50, 250))
        screen.blit(score_surface, (20, -10))
        button_back.update()
        button_guess.update()

        #--------------------- Button letters
        button_a = createButton("a", 50, 500)
        button_b = createButton("b", 100, 500)
        button_c = createButton("c", 150, 500)
        button_d = createButton("d", 200, 500)
        button_e = createButton("e", 250, 500)
        button_f = createButton("f", 300, 500)
        button_g = createButton("g", 350, 500)
        button_h = createButton("h", 400, 500)
        button_i = createButton("i", 450, 500)
        button_j = createButton("j", 75, 550)
        button_k = createButton("k", 125, 550)
        button_l = createButton("l", 175, 550)
        button_m = createButton("m", 225, 550)
        button_n = createButton("n", 275, 550)
        button_o = createButton("o", 325, 550)
        button_p = createButton("p", 375, 550)
        button_q = createButton("q", 425, 550)
        button_r = createButton("r", 50, 600)
        button_s = createButton("s", 100, 600)
        button_t = createButton("t", 150, 600)
        button_u = createButton("u", 200, 600)
        button_v = createButton("v", 250, 600)
        button_w = createButton("w", 300, 600)
        button_x = createButton("x", 350, 600)
        button_y = createButton("y", 400, 600)
        button_z = createButton("z", 450, 600)
        #----------------- Button letter update
        button_a.update()
        button_b.update()
        button_c.update()
        button_d.update()
        button_e.update()
        button_f.update()
        button_g.update()
        button_h.update()
        button_i.update()
        button_j.update()
        button_k.update()
        button_l.update()
        button_m.update()
        button_n.update()
        button_o.update()
        button_p.update()
        button_q.update()
        button_r.update()
        button_s.update()
        button_t.update()
        button_u.update()
        button_v.update()
        button_w.update()
        button_x.update()
        button_y.update()
        button_z.update()
        #--------------------------------------
        displayingame(display_in_game)

        letter = ""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.check_position_input(mouse_position):
                    title_screen(1)
                elif button_a.check_position_input(mouse_position):
                    letter = "a"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_b.check_position_input(mouse_position):
                    letter = "b"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_c.check_position_input(mouse_position):
                    letter = "c"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_d.check_position_input(mouse_position):
                    letter = "d"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_e.check_position_input(mouse_position):
                    letter = "e"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_f.check_position_input(mouse_position):
                    letter = "f"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_g.check_position_input(mouse_position):
                    letter = "g"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_h.check_position_input(mouse_position):
                    letter = "h"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_i.check_position_input(mouse_position):
                    letter = "i"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_j.check_position_input(mouse_position):
                    letter = "j"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_k.check_position_input(mouse_position):
                    letter = "k"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_l.check_position_input(mouse_position):
                    letter = "l"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_m.check_position_input(mouse_position):
                    letter = "m"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_n.check_position_input(mouse_position):
                    letter = "n"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_o.check_position_input(mouse_position):
                    letter = "o"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_p.check_position_input(mouse_position):
                    letter = "p"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_q.check_position_input(mouse_position):
                    letter = "q"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_r.check_position_input(mouse_position):
                    letter = "r"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_s.check_position_input(mouse_position):
                    letter = "s"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_t.check_position_input(mouse_position):
                    letter = "t"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_u.check_position_input(mouse_position):
                    letter = "u"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_v.check_position_input(mouse_position):
                    letter = "v"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_w.check_position_input(mouse_position):
                    letter = "w"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_x.check_position_input(mouse_position):
                    letter = "x"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_y.check_position_input(mouse_position):
                    letter = "y"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
                elif button_z.check_position_input(mouse_position):
                    letter = "z"
                    checkletter(letter, mistery_word, list_of_used_letter, display_in_game, display, nbr_chance)
        
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
                    play_page(0, 0)

        screen.blit(background_surface, (0, 0))
        screen.blit(name_game_surface, (250, 200))
        button_play.update()
        button_record.update()
        button_quit.update()
        pygame.display.update()
        # pygame.display.flip()

title_screen(1)
#-----------------------------------------------------------------------------------------
