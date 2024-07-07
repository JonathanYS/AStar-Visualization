# A* Visualization

A simple A* algorithm visualization, using pygame.

TOC - Time Of Completion = 2 hours.


Hello. I wrote this fine program to show and implement the A* algorithm in an easy-to-understand format. In addition, because I didn't use the pygame library before, I saw a great opportunity in this project to both, use the pygame library for the first time, and implement one of the greatest algorithms for pathfinding.
I must say, I had a wonderful time working on this project.

## Instructions Of The "Game"

When you first start the "game", you will see a start tile (in $\textcolor{#37FF48}{\text{green}}$) and the target tile (in $\textcolor{#FA272E}{\text{red}}$) will be marked where your mouse is placed in the window of the game (more accurately, in the frame of the game's window).
If you want to place obstacles, you need to `right click` on the mouse, anywhere in the "game's" window. Of course, you can't place an obstacle where the start tile is.
Obstacles are marked in $\textcolor{#060028}{\text{dark purple}}$ (dark purple).
The shortest path, determined by the A* algorithm is marked in $\textcolor{#3C69FA}{\text{blue}}$.

If you would like to remove a specific obstacle, just stand on it with your mouse and `right-click` it.

If you would like to remove all of the obstacles that are placed on the grid, press the `c` key on your keyboard.

If you would like to switch the starting position of the start tile, all you need to do is `left click` one of the tiles on the grid of this program. Of course, you can't place the start tile where there is already an obstacle.

## External Technologies In Use

You may witness the external technologies in use of this project in the requirments.txt file.

In general, it consists of `pygame` and `darkdetect`.

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](https://github.com/JonathanYS/AStar-Visualization/blob/main/LICENSE) file for details.
