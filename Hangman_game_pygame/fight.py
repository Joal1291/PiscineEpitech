import pygame
import time



def vegeta_waiting(position_x, position_y, screen):
    animation = 1

    while True:
        if animation == 10:
            time.sleep(0.1)
            image = pygame.image.load(f"image/fight_sprites/vegeta/pose_depart/{animation}.png")
            screen.blit(image, (position_x, position_y))
            # animation = 1
            pygame.display.flip()
            pygame.display.update()
            break
        else:
            time.sleep(0.1)
            image = pygame.image.load(f"image/fight_sprites/vegeta/pose_depart/{animation}.png")
            screen.blit(image, (position_x, position_y))
            animation += +1
            pygame.display.flip()
            pygame.display.update()



def goku_waiting(position_x, position_y, screen):
    animation = 1

    while True:
        if animation == 10:
            time.sleep(0.1)
            image = pygame.image.load(f"image/fight_sprites/goku/position_hors_combat/{animation}.png")
            screen.blit(image, (position_x, position_y))
            # animation = 1
            pygame.display.flip()
            pygame.display.update()
            break
        else:
            time.sleep(0.1)
            image = pygame.image.load(f"image/fight_sprites/goku/position_hors_combat/{animation}.png")
            screen.blit(image, (position_x, position_y))
            animation += +1
            pygame.display.flip()
            pygame.display.update()

