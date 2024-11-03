# Modules
from operator import truediv

import pygame
import random

# Data Definitions
RES = 16
DIMS = (28, 28)
SCREEN = (RES * DIMS[0], RES * DIMS[1])
display = pygame.display.set_mode(SCREEN)
LABEL = "Angry"
PATH = "./images/Angry"

# DD. TILE
# tile = TILE()
# interp. a square of dimensions RES x RES located somewhere in the SCREEN
class Tile:
    def __init__(self, c, r):
        self.c = c
        self.r = r
        self.x = self.c * RES
        self.y = self.r * RES
        self.state = 0
        self.rect = pygame.Rect(self.x, self.y, RES, RES)

    def draw(self):
        pygame.draw.rect(display, self.getColor(), self.rect)

    def getColor(self):
        if self.state == 0:
            return "black"
        return "white"

## DD. ROW
## row = [TILE]
# DD. GRID
# grid = [[TILE, ..., n = DIMS[0]], ..., n = DIMS[1]]
# interp. a 2D array of TILE
grid = []
for r in range(DIMS[1]):
    row = []
    for c in range(DIMS[0]):
        tile = Tile(c, r)
        row.append(tile)
    grid.append(row)

#/ TEMPLATE FOR GRID
#/ for row in grid:
#/   for tile in row:
#/       ... tile

# DD. ISMOUSEDOWN
# isMouseDown = boolean
# interp. whether or not the mouse is held down
isMouseDown = False

# Code

def draw():
    display.fill("red")
    for row in grid:
        for tile in row:
            tile.draw()
    pygame.display.flip()

def assignID():
    id = ""
    for _ in range(6):
        id += str(random.randint(0, 9))
    return id

def reset():
    for row in grid:
        for tile in row:
            tile.state = 0

def update():
    global isMouseDown
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            isMouseDown = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            isMouseDown = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                file = f"{PATH}/{LABEL}_{assignID()}.png"
                pygame.image.save(display, file)
                reset()

    if isMouseDown:
        for row in grid:
            for tile in row:
                if tile.rect.collidepoint(pygame.mouse.get_pos()):
                    tile.state = 1

while True:
    draw()
    update()

#if event.button == 1:
#    for row in grid:
#        for tile in row:
#            if tile.rect.collidepoint(pygame.mouse.get_pos()):
#                tile.state = 1