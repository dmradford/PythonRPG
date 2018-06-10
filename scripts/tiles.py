import pygame
import xml.etree.ElementTree as ET

pygame.init()


class Tiles:

    # Default Tile Size
    Size = 32

    @staticmethod
    def load_tileset(file):
        tiles = {}
        tile = 0

        tree = ET.parse(file)
        root = tree.getroot()
        bitmap = pygame.image.load(root[0].attrib["source"][3:])
        width = int(root[0].attrib["width"])
        height = int(root[0].attrib["height"])
        surface = pygame.Surface((width, height), pygame.HWSURFACE | pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        tilecount = int(root.attrib["tilecount"])
        columns = int(root.attrib["columns"])
        rows = int(tilecount / columns)
        Size = int(root.attrib["tilewidth"])

        for tr in range(rows):
            for tc in range(columns):
                tile += 1
                tiles[str(tile)] = surface.subsurface(
                    pygame.Rect(tc * Size, tr * Size, Size, Size))

        return tiles