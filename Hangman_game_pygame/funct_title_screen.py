import pygame as py
import random
import time

def title_screen_animation(b):

    py.mixer.music.load("musique/music230sec.mp3")
    py.mixer.music.play()
    py.mixer.music.set_volume(0.3)
    animation = 1
    title_apparition = 0
    while animation <= 208:
        image_name = py.image.load("image/namegamewhite.png")
        image = py.image.load(f"image_anim_title_screen/output_image_{animation}.png")
        if animation < 208:
            time.sleep(0.1)
            b.blit(image, (0,0))
            animation += 1

            image_name.set_alpha(title_apparition)
            b.blit(image_name, (250, 200))
            title_apparition += 1
            py.display.flip()

        else:
            b.blit(image, (0, 0))
            break

        
