import pgzrun

GRID_WIDTH = 64
GRID_HEIGHT = 64
GRID_SIZE = 50

WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

MAP = ["WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W"<
 "W                                                              W",
 "W                                                              W",
 "W                        WWWWWW WWWWWWWWW                      W",
 "W                        W    WWW       W                      W",
 "W                        W                                     W",
 "W                        WWWWWWWWWWWWWWWW                      W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                             WW  WW                           W",
 "W                             W    W                           W",
 "W                             W    W                           W",
 "W                             W    W                           W",
 "W                             W    W                           W",
 "W                             WWWWWW                           W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "W                                                              W",
 "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"]

def screen_coords(x, y):
  return (x * GRID_SIZE, y * GRID_SIZE)
def draw_background():
  for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
      screen.blit("chiseled_stone_bricks_tile_texture", screen_coords(x, y))

def draw():
  draw_background()

pgzrun.go()