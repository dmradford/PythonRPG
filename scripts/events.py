import pygame
from .globals import *

pygame.init()


class Events:
    @staticmethod
    def get_events():
        for event in pygame.event.get():
            # keyboard_events = ()
            if event.type == pygame.KEYDOWN: # or event.type == pygame.KEYUP:
                key_state = pygame.key.get_pressed()

                if key_state[pygame.K_w] and not key_state[pygame.K_s]:
                    Globals.char_move[0] = 1
                else:
                    Globals.char_move[0] = 0

                if key_state[pygame.K_s] and not key_state[pygame.K_w]:
                    Globals.char_move[1] = 1
                else:
                    Globals.char_move[1] = 0

                if key_state[pygame.K_a] and not key_state[pygame.K_d]:
                    Globals.char_move[2] = 1
                else:
                    Globals.char_move[2] = 0

                if key_state[pygame.K_d] and not key_state[pygame.K_a]:
                    Globals.char_move[3] = 1
                else:
                    Globals.char_move[3] = 0

                if key_state[pygame.K_ESCAPE]:
                    Globals.isRunning = False

                return key_state

            #return keyboard_events
