from .globals import *
from .tiles import *
from .events import *


class Character:
    def __init__(self, window: pygame.display, sprites: dict, t_path: str):
        """Initializes a Character object, must be within a window"""
        self.window = window
        self.char_Location = [160, 160]
        self.char_move = [0, 0, 0, 0]
        self.char_speed = .1
        self.sprite = 1
        self.sprites = sprites
        self.tiles = Tiles.load_tileset(t_path)

    def __parse_events(self):
        input_keys = Events.get_keyboard()
        if input_keys is not None and len(input_keys) > 50:
            print("Found keyboard input!")
            """Designates movement properties based on keyboard input"""
            if input_keys[pygame.K_w] and not input_keys[pygame.K_s]:
                self.char_move[0] = 1
            else:
                self.char_move[0] = 0

            if input_keys[pygame.K_s] and not input_keys[pygame.K_w]:
                self.char_move[1] = 1
            else:
                self.char_move[1] = 0

            if input_keys[pygame.K_a] and not input_keys[pygame.K_d]:
                self.char_move[2] = 1
            else:
                self.char_move[2] = 0

            if input_keys[pygame.K_d] and not input_keys[pygame.K_a]:
                self.char_move[3] = 1
            else:
                self.char_move[3] = 0

    def move(self):
        print("Checking for keyboard input")
        self.__parse_events()

        """Provides movement capabilities based on the events"""
        local_speed = sum(self.char_move) * self.char_speed

        if local_speed > self.char_speed:
            local_speed = local_speed * .33

        if self.char_move[0] == 1:
            self.char_Location[1] -= local_speed
        if self.char_move[1] == 1:
            self.char_Location[1] += local_speed
        if self.char_move[2] == 1:
            self.char_Location[0] -= local_speed
        if self.char_move[3] == 1:
            self.char_Location[0] += local_speed
        print("Character movement: " + str(self.char_move))

        if local_speed == self.char_speed:
            if self.char_move[0] == 1:
                Character.sprite = 1
            elif self.char_move[1] == 1:
                Character.sprite = 2
            elif self.char_move[2] == 1:
                Character.sprite = 3
            elif self.char_move[3] == 1:
                Character.sprite = 4

        self.window.blit((self.tiles[self.sprites[self.sprite]]), (self.char_Location[0], self.char_Location[1]))

        # Below adds tiles the Character was covering to the Global dirty tiles list
        Globals.dirtyTiles.append(
            [int(round((self.char_Location[0] - 15) / 32)),
             int(round((self.char_Location[1] - 16) / 32))]
            )
        Globals.dirtyTiles.append(
            [int(round((self.char_Location[0] + 15) / 32)),
                int(round((self.char_Location[1] - 16) / 32))]
            )
        Globals.dirtyTiles.append(
            [int(round((self.char_Location[0] - 15) / 32)),
                int(round((self.char_Location[1] + 15) / 32))]
            )
        Globals.dirtyTiles.append(
            [int(round((self.char_Location[0] + 15) / 32)),
                int(round((self.char_Location[1] + 15) / 32))]
            )
