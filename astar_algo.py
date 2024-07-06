"""
This program was written by Yonatan Deri.
"""
from node import Node
import heapq
import math


MAX_BORDER_VALUE = 19
MIN_BORDER_VALUE = 0

# Define relative positions around the center tile.
relative_positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


class AStar:
    """
    This class is responsible for the actual implementation of the A* algorithm.
    """
    def __init__(self, start: tuple[int, int], target: tuple[int, int], obstacles: set):
        """
        This function is the build function of the AStar class.
        It returns an object that is responsible for
        finding the shortest path from the source tile to the destination tile.
        :param start:
        :param target:
        :param obstacles:
        """
        self.start = start
        self.target = target

        self.obstacles = obstacles
        self.cells = dict()
        for row in range(MAX_BORDER_VALUE + 1):
            for column in range(MAX_BORDER_VALUE + 1):
                self.cells[(column, row)] = Node()
        start_h_cost = self.calculate_h_cost(self.start)
        self.cells[self.start] = Node(parent=(-1, -1), g=0.0, h=start_h_cost,
                                      f=start_h_cost)
        self.open = [(start_h_cost, self.start)]
        heapq.heapify(self.open)
        self.route = []

    def is_obstacle(self, tile: tuple[int, int]) -> bool:
        """
        This function is responsible for checking if the received tile position is an obstacle.
        :param tile:
        :return bool:
        """
        return tile in self.obstacles

    def is_destination(self, tile: tuple[int, int]) -> bool:
        """
        This function is responsible for checking if the received tile position is the destination.
        :param tile:
        :return bool:
        """
        return tile == self.target

    def calculate_h_cost(self, tile: tuple[int, int]) -> float:
        """
        This function is responsible for calculating the h cost (Euclidean distance to destination).
        :param tile:
        :return float:
        """
        # Calculate the heuristic value of a cell (Euclidean distance to destination - based on the Pythagorean theorem)
        return math.sqrt((tile[0] - self.target[0]) ** 2 + (tile[1] - self.target[1]) ** 2)

    def main_function(self) -> tuple[int, list]:
        """
        This is the main function of the AStar class.
        It is responsible for the managing of this algorithm (A*).
        :return tuple:
        """
        while self.open:
            p = heapq.heappop(self.open)[1]  # Pop node with lowest f cost.

            if self.is_destination(p):
                # Reconstruct the path.
                pos = p
                while pos != (-1, -1):
                    self.route.append(pos)
                    pos = self.cells[pos].parent
                self.route.reverse()  # Reverse to get path from start to target.
                return 1, self.route

            if self.cells[p].visited:
                continue

            self.cells[p].visited = True
            surrounded_tiles = get_surrounding_tiles(p)

            for direction in surrounded_tiles:
                if self.is_obstacle(direction):
                    continue
                g_new = self.cells[p].g + 1.0
                h_new = self.calculate_h_cost(direction)
                f_new = g_new + h_new

                if self.cells[direction].f == 0.0 or self.cells[direction].f > f_new:
                    self.cells[direction] = Node(parent=p, g=g_new, h=h_new, f=f_new)
                    heapq.heappush(self.open, (f_new, direction))
        return -1, []


def border_safe(value: int) -> bool:
    """
    This function is responsible for notifying if a given value is within the grid borders.
    :param value:
    :return bool:
    """
    return MAX_BORDER_VALUE >= value >= MIN_BORDER_VALUE


def get_surrounding_tiles(current_tile: tuple[int, int]) -> list:
    """
    This function is responsible for getting the surrounding tiles of a given tile in a list
    (only if these tiles are withing the borders of the grid).
    :param current_tile:
    :return list:
    """
    list_of_current_tile = list(current_tile)
    surrounding_tiles = [(list_of_current_tile[0] + dy, list_of_current_tile[1] + dx) for dy, dx in relative_positions]
    final_list = []
    for tile in surrounding_tiles:
        if border_safe(tile[0]) and border_safe(tile[1]):
            final_list.append(tile)
    return final_list
