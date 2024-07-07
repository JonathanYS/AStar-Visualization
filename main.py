"""
This program was written by Yonatan Deri.
"""

import pygame
import logging
from astar_algo import AStar
import darkdetect

pygame.init()
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logging.info("The program has been started.")


# Window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("A* algorithm visualization - written by Yonatan Deri.")

# Colors
BG = (60, 60, 60)  # Background color
GREY = (50, 50, 50)  # Tile color
GREEN = "#37FF48"  # Start color
RED = "#FA272E"  # Target color
BLUE = "#3C69FA"  # Surrounding color
DARK_PURPLE = "#060028"  # Obstacle color

# "Game" variables
TILE_SIZE = 30

# Clock object
clock = pygame.time.Clock()
FPS = 300


start_position = (0, 0)
target_position = (19, 19)
obstacles = set()

if darkdetect.isDark() is True:
    program_icon = pygame.image.load("images\\a_with_asterisk_light.png")
    pygame.display.set_icon(program_icon)
else:
    program_icon = pygame.image.load("images\\a_with_asterisk_dark.png")
    pygame.display.set_icon(program_icon)


def highlight_tile(tile: tuple[int, int], color: str | tuple[int, int, int]) -> None:
    """
    This function is responsible for highlighting a specific tile in the grid with a specific color.
    :param tile:
    :param color:
    :return None:
    """
    # Calculate position to highlight
    highlight_x = tile[0] * TILE_SIZE
    highlight_y = tile[1] * TILE_SIZE
    # Draw highlight rectangle
    pygame.draw.rect(SCREEN, color, (highlight_x, highlight_y, TILE_SIZE, TILE_SIZE))


def draw_grid() -> None:
    """
    This function is responsible for drawing the grid.
    :return None:
    """
    global target_position, obstacles
    # Fill screen
    SCREEN.fill(BG)

    # Draw vertical lines
    for y in range(TILE_SIZE, SCREEN_WIDTH, TILE_SIZE):
        pygame.draw.line(SCREEN, GREY, (y, 0), (y, SCREEN_HEIGHT))

    # Draw horizontal lines
    for x in range(TILE_SIZE, SCREEN_HEIGHT, TILE_SIZE):
        pygame.draw.line(SCREEN, GREY, (0, x), (SCREEN_WIDTH, x))

    highlight_tile(tile=start_position, color=GREEN)
    for obstacle in obstacles:
        highlight_tile(tile=obstacle, color=DARK_PURPLE)


def draw_path(route: list) -> None:
    """
    This function is responsible for drawing the path to the target tile.
    :param route:
    :return None:
    """
    global start_position, target_position
    for tile in route:
        if tile != start_position and tile != target_position:
            highlight_tile(tile=tile, color=BLUE)


def set_target(position: tuple[int, int], forced: bool = False) -> None:
    """
    This function is responsible for setting the target tile using the user's cursor position.
    :param position:
    :param forced:
    :return None:
    """
    global target_position
    if position != target_position and forced is False:
        highlight_tile(tile=target_position, color=BG)
        draw_grid()
        position_list = list(position)
        tile = (position_list[0] // TILE_SIZE, position_list[1] // TILE_SIZE)
        highlight_tile(tile=tile, color=RED)

        target_position = tile
    else:
        if forced is True:
            highlight_tile(tile=target_position, color=BG)
            draw_grid()
            position_list = list(position)
            tile = (position_list[0] // TILE_SIZE, position_list[1] // TILE_SIZE)
            highlight_tile(tile=tile, color=RED)

            target_position = tile


def add_obstacle(position: tuple[int, int]) -> None:
    """
    This function is responsible for adding or removing an obstacle
    to the current grid by the mouse position where the mouse's
    right click has been pressed by the user (by the position argument).
    :param position:
    :return None:
    """
    global obstacles
    position_list = list(position)
    tile = (position_list[0] // TILE_SIZE, position_list[1] // TILE_SIZE)
    if tile != start_position:
        if tile in obstacles:
            obstacles.remove(tile)
            draw_grid()
            set_target(target_position, forced=True)
        else:
            obstacles.add(tile)
            highlight_tile(tile=tile, color=DARK_PURPLE)


def clean_obstacles() -> None:
    """
    This function is responsible for cleaning all of the obstacles that are on the grid.
    :return None:
    """
    global obstacles, target_position
    obstacles = set()
    draw_grid()
    set_target(target_position, forced=True)


def switch_start_position(position: tuple[int, int]) -> None:
    """
    This function is responsible for switching the start tile of this program on the grid to where the user left
    clicked using his mouse.
    :param position:
    :return None:
    """
    global start_position, obstacles
    position_list = list(position)
    tile = (position_list[0] // TILE_SIZE, position_list[1] // TILE_SIZE)
    if tile != start_position and tile not in obstacles:
        start_position = tile
        draw_grid()


def main() -> None:
    """
    This is the main function of this program.
    It is responsible for handling the entire program using the various available functions.
    :return None:
    """
    global target_position, obstacles
    run = True

    # Draw grid
    draw_grid()

    # Main Loop
    while run is True:
        # Set frame rate
        clock.tick(FPS)

        position = pygame.mouse.get_pos()
        position_list = list(position)
        tile = (position_list[0] // TILE_SIZE, position_list[1] // TILE_SIZE)
        response, route = AStar(start=start_position, target=target_position, obstacles=obstacles).main_function()
        if response == 1:
            draw_path(route)
        if target_position != tile:
            set_target(position)

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    clean_obstacles()
            if event.type == pygame.MOUSEBUTTONUP:
                match event.button:
                    case 3:  # Right click.
                        add_obstacle(pygame.mouse.get_pos())
                    case 1:  # Left click.
                        switch_start_position(pygame.mouse.get_pos())

        pygame.display.update()

    logging.info("Exiting the program cleanly.")
    pygame.quit()


if __name__ == '__main__':
    """
    This is an "if statement" to check if this program is being ran directly, and not by another program.
    """
    main()
