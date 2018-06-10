import pygame
import time
from .globals import *


class Debug:
    debug = True
    cSec = 0
    cFrame = 0
    FPS = 0

    debug_font = pygame.font.Font(None, 20)

    def show_fps(window):
        fps_overlay = Debug.debug_font.render(str(Debug.FPS),
            True, (255, 255, 255))
        window.blit(fps_overlay, (10, 10))

    def show_charLoc(window):
        xLoc = Debug.debug_font.render("X: "
            + str(round(Globals.char_Location[0], 2)), True, (255, 255, 255))
        yLoc = Debug.debug_font.render("Y: "
            + str(round(Globals.char_Location[1], 2)), True, (255, 255, 255))
        window.blit(xLoc, (10, 25))
        window.blit(yLoc, (10, 40))

    def count_fps():
        global cSec, cFrame, FPS

        if Debug.cSec == time.strftime("%S"):
            Debug.cFrame += 1
        else:
            Debug.FPS = Debug.cFrame
            Debug.cFrame = 0
            Debug.cSec = time.strftime("%S")
