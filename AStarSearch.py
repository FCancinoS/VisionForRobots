# -*- coding: utf-8 -*-
"""
@author:José Andrés Miguel Martinez A01653368
Juan Carlos Garza Sánchez A00821522
Francisco Cancino Sastré A01730698
Ian Airy Suárez Barrientos A00818291
Cristian Palma Martinez A01244565

"""
import collections

import untitled3
import cv2
import numpy as np


class Queue:
    """Clase para implementar una lista FIFO"""

    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        """Regresa el objeto más antiguo"""
        return self.elements.popleft()


caminos = []


class SquareGrid:
    """A class to represent a grid map with obstacles."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 < x <= self.width and 0 < y <= self.height

    def passable(self, id):
        return id not in self.walls  # not passable nodes are walls

    def neighbors(self, id):
        """Return neighboring passable nodes."""
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0: results.reverse()  # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def draw(self, goal=None, route=None):
        """Print a representation of the grid."""
        grid = [[' . ' for _ in range(self.width)] for _ in range(self.height)]

        def modify_grid(symbol, i, j):
            grid[self.height - j][i - 1] = symbol

        for node in self.walls:
            modify_grid(' # ', *node)

        if goal:
            modify_grid(' X ', *goal)

        # print the directions traversed along a route
        if route:
            comes = route[goal]
            goes = goal
            step = 0

            while comes:
                x1, y1 = comes
                x2, y2 = goes
                xdir = x2 - x1
                ydir = y2 - y1
                caminos.append((y1, x1))
                if xdir > 0:
                    modify_grid(' > ', *comes)
                elif xdir < 0:
                    modify_grid(' < ', *comes)
                elif ydir > 0:
                    modify_grid(' ^ ', *comes)
                else:
                    modify_grid(' v ', *comes)
                goes = comes
                comes = route[comes]
                step += 1
            print("Number of steps:", step)

        for row in grid:
            print(''.join(row))


grid = SquareGrid(untitled3.mem_y, untitled3.mem_x)
start = (2, 4)
goal = (23, 26)
grid.walls = untitled3.pard_list
# grid = SquareGrid(23, 23)
# start = (1, 1)
# goal = (12, 12)
# grid.walls = [(5, 8), (6, 7), (1, 23), (2, 23), (3, 23), (4, 23),
#               (5, 23), (6, 23), (7, 23), (8, 23), (1, 22), (2, 22), (3, 22),
#               (4, 22), (5, 22), (6, 22), (7, 22), (5, 21), (6, 21), (10, 21),
#               (11, 21), (12, 21), (13, 21), (14, 21), (19, 21), (20, 21), (21, 21),
#               (9, 20), (15, 20), (19, 20), (20, 20), (21, 20), (3, 19),
#               (8, 19), (16, 19), (20, 19), (21, 19), (3, 18), (4, 18), (7, 18), (11, 18), (12, 18), (13, 18), (15, 18),
#               (16, 18), (17, 18), (20, 18), (21, 18), (4, 17), (5, 17), (6, 17), (10, 17), (14, 17), (15, 17), (16, 17),
#               (17, 17), (20, 17), (21, 17), (1, 16), (5, 16), (9, 16), (20, 16), (21, 16), (8, 15), (12, 15), (20, 15),
#               (21, 15), (3, 14), (7, 14), (11, 14), (13, 14), (17, 14), (18, 14), (19, 14), (20, 14), (21, 14), (4, 13),
#               (6, 13), (10, 13), (14, 13), (18, 13), (19, 13), (20, 13), (21, 13), (1, 12), (5, 12), (9, 12), (15, 12),
#               (19, 12), (21, 12), (2, 11), (6, 11), (14, 11), (18, 11), (3, 10), (7, 10), (13, 10), (17, 10), (4, 9),
#               (8, 9), (12, 9), (16, 9), (20, 9), (9, 8), (15, 8), (21, 8), (10, 7), (14, 7), (18, 7), (22, 7), (3, 6),
#               (7, 6), (11, 6), (13, 6), (17, 6), (19, 6), (23, 6), (4, 5), (8, 5), (12, 5), (16, 5), (20, 5), (5, 4),
#               (9, 4), (13, 4), (15, 4), (21, 4), (6, 3), (10, 3), (14, 3), (18, 3), (3, 2), (17, 2), (18, 2), (19, 2),
#               (3, 1), (4, 1), (8, 1), (12, 1), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (23, 1)]
grid.draw(goal=goal)


class GridWithWeights(SquareGrid):
    """A class to represent a grid with weights."""

    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)


import heapq


class PriorityQueue:
    """A class to implement priority queues.
    Each node is less or equal to its children, and the root
    is the smallest value in the queue.
    """

    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        """Return item with smallest priority value."""
        return heapq.heappop(self.elements)[1]


diagram4 = GridWithWeights(grid.width, grid.height)
diagram4.walls = grid.walls
# =========== Challenge 5 =============================
# Here the step costs are unitary, you need to change
# them to non-unitary costs ...
# Change the step costs to achieve the desired route!
# =====================================================

diagram4.weights = {(x, y): 0 for x in range(grid.width + 1) for y in range(grid.height + 1)}


def heuristic(a, b):
    """Return estimated cost between two points."""

    (x1, y1) = a
    (x2, y2) = b
    # =========== Challenge 6 =============
    # heuristica = ...
    heuristica = abs(-x2 + x1) + abs(-y2 + y1)
    # =====================================

    return heuristica


def a_star_search(graph, start, goal):
    """Search for least costly path along expanding frontier with heuristic."""
    frontier = PriorityQueue()
    frontier.put(start, 0)  # start position has cost 0
    came_from = {}  # stores the parent node
    cost_so_far = {}  # cost from start to current node
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            # ignore already traversed nodes unless new route is less costly
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                # =========== Challenge 8 =============
                # priority = ... (fev)
                priority = heuristic(goal, next) + cost_so_far[current] + graph.weights[next]
                # =====================================

                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


diagram4.weights = {(x, y): 1 for x in range(grid.width + 1) for y in range(grid.height + 1)}
came_from, cost_so_far = a_star_search(diagram4, start, goal)
diagram4.draw(route=came_from, goal=goal)

# caminos se gurada la lista de los pasos a seguir
path_map = untitled3.mem.copy()
# path_map = np.zeros((untitled3.mem_y, untitled3.mem_x), dtype=np.uint8)

for idx in caminos:
    path_map[idx[1], idx[0]] = 127

# mem3 = np.reshape(untitled3.mem, (untitled3.mem_y,untitled3.mem_x,3))
# 
# path_map2 = np.add(path_map,untitled3.mem)
path_map2 = cv2.resize(path_map, (450, 450), interpolation=cv2.INTER_AREA)
cv2.imshow('Ruta ', path_map2)
cv2.imwrite('/Photos/Map.png', untitled3.mem2)
cv2.imwrite('Photos/Map_rout.png', path_map2)
cv2.imwrite('Photos/segment.png', untitled3.img_d)

color_map = np.zeros((450, 450, 3), np.uint8)

for i in range(450):
    for j in range(450):
        if path_map2[i, j] == 255:
            color_map[i, j, :] = [255, 255, 255]
        elif path_map2[i, j] == 127:
            color_map[i, j, :] = [0, 0, 255]
        else:
            color_map[i, j, :] = [0, 0, 0]


x = lambda a : (a[0]*(60//4),a[1]*(50//3))

for idx in range (1,(len(caminos))):
    cv2.line(untitled3.img,x(caminos[idx-1]),x(caminos[idx]),(255,0,0),5)

cv2.imshow('color',untitled3.img)
cv2.imwrite('Photos/color_mpa_route.png',untitled3.img)
cv2.imwrite('Photos/Mapa_route_color.png',color_map)



cv2.waitKey(0)
