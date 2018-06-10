import sys
from scripts.map import *
from scripts.debug import *
from scripts.events import *
from scripts.character import *

pygame.init()

worldMap = Map().load_map("maps/Map1.tmx")


def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 480
    window_title = 'RPG'
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height),
                                     pygame.HWSURFACE | pygame.DOUBLEBUF)


create_window()

# - Render worldMap
for key in sorted(worldMap):
    for row in range(len(worldMap[key])):
        for column in range(len(worldMap[key][row])):
            window.blit(worldMap[key][row][column],
                        (column * Tiles.Size, row * Tiles.Size))

character = Character(window, {1: "1", 2: "10", 3: "4", 4: "7"}, "tilesets/characterSheet_Boy.tsx")

while Globals.isRunning:

    # Collect events
    Events.get_events()

    # Logic

    # Redraw dirty tiles
    for key in sorted(worldMap):
        for tile in Globals.dirtyTiles:
            column = tile[0]
            row = tile[1]
            window.blit(worldMap[key][row][column], (column * 32, row * 32))
    Globals.dirtyTiles = []

    # Draw character and mark tiles as dirty
    local_speed = sum(Globals.char_move) * Globals.char_speed

    if local_speed > Globals.char_speed:
        local_speed = local_speed * .33

    if Globals.char_move[0] == 1:
        Globals.char_Location[1] -= local_speed
    if Globals.char_move[1] == 1:
        Globals.char_Location[1] += local_speed
    if Globals.char_move[2] == 1:
        Globals.char_Location[0] -= local_speed
    if Globals.char_move[3] == 1:
        Globals.char_Location[0] += local_speed
    #print("Character movement: " + str(self.char_move))

    if local_speed == Globals.char_speed:
        if Globals.char_move[0] == 1:
            Character.sprite = 1
        elif Globals.char_move[1] == 1:
            Character.sprite = 2
        elif Globals.char_move[2] == 1:
            Character.sprite = 3
        elif Globals.char_move[3] == 1:
            Character.sprite = 4

    window.blit((Globals.tiles[Globals.sprites[Globals.sprite]]), (Globals.char_Location[0], Globals.char_Location[1]))

    # Below adds tiles the Character was covering to the Global dirty tiles list
    Globals.dirtyTiles.append(
        [int(round((Globals.char_Location[0] - 15) / 32)),
         int(round((Globals.char_Location[1] - 16) / 32))]
    )
    Globals.dirtyTiles.append(
        [int(round((Globals.char_Location[0] + 15) / 32)),
         int(round((Globals.char_Location[1] - 16) / 32))]
    )
    Globals.dirtyTiles.append(
        [int(round((Globals.char_Location[0] - 15) / 32)),
         int(round((Globals.char_Location[1] + 15) / 32))]
    )
    Globals.dirtyTiles.append(
        [int(round((Globals.char_Location[0] + 15) / 32)),
         int(round((Globals.char_Location[1] + 15) / 32))]
    )

    # Show Debug info
    if Debug.debug is True:
        Debug.show_fps(window)
        Debug.show_charLoc(window)
        for x in range(3):
            for y in range(2):
                Globals.dirtyTiles.append([x, y])
        Debug.count_fps()

    pygame.display.update()

pygame.quit()
sys.exit()
