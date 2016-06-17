"""
The labyrinth has no walls, but bushes surround the path on each side.
If a players move into a bush, they lose. The labyrinth is presented as a
matrix (a list of lists): 1 is a bush and 0 is part of the path. T
he labyrinth's size is 12 x 12 and the outer cells are also bushes.
Players start at cell (1,1). The exit is at cell (10,10).
You need to find a route through the labyrinth. Players can move in only four
directions--South (down [1,0]), North (up [-1,0]), East (right [0,1]),
West (left [0, -1]). The route is described as a string consisting of different
characters: "S"=South, "N"=North, "E"=East, and "W"=West.
"""

from collections import defaultdict, deque
from pprint import pprint


# https://en.wikipedia.org/wiki/Breadth-first_search
def breadth_first_search(graph, start, stop):
    queue = deque([(start, '')])
    visited_nodes = set()
    while queue:
        node, path = queue.popleft()
        if node == stop:
            return path

        if node not in visited_nodes:
            visited_nodes.add(node)
            queue.extend(
                [(next_node, path + direction)
                 for direction, next_node in graph[node]])
        else:
            continue


def labyrinth_to_graph(labyrinth):

    graph = defaultdict(list)

    get_cell = lambda _labyrinth, _row, _col: _labyrinth[_row][_col]

    labyrinth_width = len(labyrinth[0]) - 1
    labyrinth_height = len(labyrinth) - 1

    for row_idx, row in enumerate(labyrinth):
        for col_idx, col in enumerate(row):

            cell = get_cell(labyrinth, row_idx, col_idx)
            if cell == 0:

                moves_from_cell = []

                # check E direction
                e_cell_idx = (row_idx, min(col_idx + 1, labyrinth_width))
                if get_cell(labyrinth, *e_cell_idx) == 0:
                    moves_from_cell.append(('E', e_cell_idx))

                # check W direction
                w_cell_idx = (row_idx, max(col_idx - 1, 0))
                if get_cell(labyrinth, *w_cell_idx) == 0:
                    moves_from_cell.append(('W', w_cell_idx))

                # check S direction
                s_cell_idx = (min(row_idx + 1, labyrinth_height), col_idx)
                if get_cell(labyrinth, *s_cell_idx) == 0:
                    moves_from_cell.append(('S', s_cell_idx))

                # check N direction
                n_cell_idx = (max(row_idx - 1, 0), col_idx)
                if get_cell(labyrinth, *n_cell_idx) == 0:
                    moves_from_cell.append(('N', n_cell_idx))

                graph[(row_idx, col_idx)] = moves_from_cell

    pprint(graph)
    return graph


def checkio(labyrinth):
    start, stop = (1, 1), (10, 10)
    graph = labyrinth_to_graph(labyrinth)
    directions = breadth_first_search(graph, start, stop)
    print(directions)
    return directions


if __name__ == "__main__":

    checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])