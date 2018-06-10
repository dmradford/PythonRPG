import xml.etree.ElementTree as ET
from .tiles import *


class Map:

    def load_map(self, file):
        tree = ET.parse(file)
        root = tree.getroot()

        # Load tileset
        # Trim first 3 characters on load to negate relative filepath
        tileSet = Tiles.load_tileset(root[0].attrib["source"][3:])

        layers = {}

        # Collect Layers
        for child in range(len(root)):
            if root[child].tag == "layer":
                layers[str(child) + "_"
                    + root[child].attrib["name"]] = root[child]

        for key in layers:  # Itterate through layers
            rows = []
            for row in layers[key][0].text.split():  # Iterate through rows
                rowTiles = []
                row = row.split(',')  # Split row into tiles

                if row[-1] == '':
                    # Remove empty list object at the end if exists
                    row = row[0:-1]
                for tile in row:
                    if tile == "0":  # Make empty tiles transparent
                        mask = pygame.Surface(
                            (Tiles.Size, Tiles.Size), pygame.SRCALPHA)
                        #mask.fill
                        mask.set_alpha(255)
                        rowTiles.append(mask)
                    else:
                        rowTiles.append(tileSet[str(tile)])
                rows.append(rowTiles)   # Add row to rows in Layer
            layers[key] = rows  # Add mapped layer to dict
        return layers
