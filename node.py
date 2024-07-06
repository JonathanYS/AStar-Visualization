"""
This program was written by Yonatan Deri.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Node:
    """
    This class is responsible for storing the nodes' information for the A* algorithm implementation.
    This information includes the parent information which shows the behaviour of a linked list.
    This linked list holds the actual shortest route found by the A* algorithm.
    """
    parent: tuple[int, int] = (0, 0)
    g: float = 0.0  # Distance from the current node to the start node.
    h: float = 0.0  # Distance from the current node to the target node.
    f: float = 0.0  # g + h = f cost.
    visited: bool = False
