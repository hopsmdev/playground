"""
DISCLAIMER:
This algorithm (finding all paths in graph) is very inefficient for
big problems set.
You can think of it like about Brute Force algorithm with very bad
time complexity O(2^n).

This is a classical problem which shows you how to use dynamic programming.
This concept is a core component of many optimisation tasks
"""

"""
Consider a tuple of tuples in which the first tuple has one integer and each
consecutive tuple has one more integer then the last. Such a tuple of tuples
would look like a triangle. You should write a program that will help Stephan
find the highest possible sum on the most profitable route down the pyramid.
All routes down the pyramid involve stepping down and to the left or down and
to the right.

Tips: Think of each step down to the left as moving to the same index location
or to the right as one index location higher. Be very careful if you plan to
use recursion here.

For example we have pyramids like:

(1,),
(2, 3),
(3, 3, 1),
(3, 1, 5, 4),
(3, 1, 3, 1, 3),
(2, 2, 2, 2, 2, 2),
(5, 6, 4, 5, 6, 4, 3)

Maximum gold count here is 23, and path is:
(0,0) 1 -> (1,1) 3 -> (2,1) 3 -> (3,2) 5 -> (4,2) 3 -> (5,3) 2 -> (6,4) 6
and it takes 23
"""


_ROOT, _DEPTH, _BREADTH = range(3)


class Node:
    def __init__(self, identifier):
        self.__identifier = identifier
        self.__children = []

    @property
    def identifier(self):
        return self.__identifier

    @property
    def children(self):
        return self.__children

    def add_child(self, identifier):
        self.__children.append(identifier)

    def __str__(self):
        return str(self.identifier)

    def __repr__(self):
        return str(self.identifier)


class Tree:
    def __init__(self):
        self.__nodes = {}

    @property
    def nodes(self):
        return self.__nodes

    def add_node(self, identifier, parent=None):
        node = Node(identifier)
        self[identifier] = node

        if parent is not None:
            self[parent].add_child(identifier)

        return node

    def display(self, identifier, depth=_ROOT):
        children = self[identifier].children
        if depth == _ROOT:
            print("{0}".format(identifier))
        else:
            print("\t"*depth, "{0}".format(identifier))

        depth += 1
        for child in children:
            self.display(child, depth)  # recursive call

    def __getitem__(self, key):
        return self.__nodes[key]

    def __setitem__(self, key, item):
        self.__nodes[key] = item


def find_all_paths(graph, start, end, path=[]):
    """
    Algorithm implementation idea taken from
    https://www.python.org/doc/essays/graphs/

    It finds all paths between start and end node in graph
    :param graph: tree like:
        (0, 0)
	        (1, 0)
		        (2, 0)
			        (3, 0)
			        (3, 1)
		        (2, 1)
			        (3, 1)
			        (3, 2)

    :param start: root node e.g.; (0, 0)
    :param end: end node e.g.: (3, 2)
    :param path:
    :return: list of all paths between start and end node in graph
    """
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph.nodes:
        return []
    paths = []
    for node in graph[start].children:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for newpath in new_paths:
                paths.append(newpath)
    return paths


def test_count_gold(pyramid):
    """
    ((1,),golden_pyramid
    (2, 3),
    (3, 3, 1),
    (3, 1, 5, 4),
    """

    tree = Tree()
    tree.add_node((0,0))  # root node
    tree.add_node((1,0), (0,0))
    tree.add_node((1,1), (0,0))
    tree.add_node((2,0), (1,0))
    tree.add_node((2,1), (1,0))
    tree.add_node((2,1), (1,1))
    tree.add_node((2,2), (1,1))
    tree.add_node((3,0), (2,0))
    tree.add_node((3,1), (2,0))
    tree.add_node((3,1), (2,1))
    tree.add_node((3,1), (2,2))
    tree.add_node((3,2), (2,1))
    tree.add_node((3,2), (2,2))
    tree.add_node((3,3), (2,2))

    tree.display((0,0))
    endpoints = [(3,1), (3,2), (3,3)]
    max_gold = []
    for endpoint in endpoints:
        paths = find_all_paths(tree, (0,0), endpoint)
        values = []
        for path in paths:
            values.append([pyramid[node[0]][node[1]] for node in path])

        max_gold_path = [sum(path) for path in values]
        max_gold.append(max(max_gold_path))

    print("MAX GOLD: ", max(max_gold))


def count_gold(pyramid):

    root_row_idx, root_col_idx = 0, 0
    root = (root_row_idx, root_col_idx)

    # create Tree with root (0, 0)
    tree = Tree()
    tree.add_node(root)  # root node

    # list of roots: [((0,0)), ((1,0), (1,1), (1, 2)) ,,,((n, n+1),(n, n+2))]
    root_col_idxs = [(row_idx, range(len(row)))
                     for row_idx, row in enumerate(pyramid[:-1])]

    for row_idx, col_idxs in root_col_idxs:  # iterate over list of roots
        for col_idx in col_idxs:
            root = (row_idx, col_idx)

            # find children nodes
            next_row = min(row_idx + 1, len(pyramid) - 1)
            next_col = min(col_idx + 1, len(pyramid[next_row]) - 1)

            # create new node in tree
            [tree.add_node(node, root) for node in
             set([(next_row, col_idx),
                  (next_row, next_col)])]

    # uncomment this to print tree
    #tree.display((0,0))

    # find tree endpoints (tree leaves)
    endpoints = [(len(pyramid[-1]) - 1, col)
                 for col in range(len(pyramid[-1]))]

    max_gold = []
    for endpoint in endpoints:  # iterate over endpoints
        # find all possible paths in tree (from root to given endpoint)
        paths = find_all_paths(tree, (0, 0), endpoint)

        # translate node coordinates to node value (values list)
        # for example from (0, 0) to 1
        values = []
        for path in paths:
            values.append([pyramid[node[0]][node[1]] for node in path])

        # sum all values for given path
        max_gold_path = [sum(path) for path in values]

        # add maximum value for path to max_gold list
        max_gold.append(max(max_gold_path))

    print("MAX GOLD: ", max(max_gold))
    return max(max_gold)


if __name__ == '__main__':

    test_count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4)))

    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"

    assert count_gold((
        [2],
        [7, 9],
        [0, 8, 6],
        [4, 7, 6, 8],
        [0, 5, 5, 4, 1],
        [9, 1, 0, 1, 6, 9])) == 35, "last example"


    """
    This algorithm is very inefficient for big problems set like this
    last pyramid - so processing may take a while ...
    """
    """
    assert count_gold((
        [4],
        [1, 7],
        [9, 9, 7],
        [4, 9, 9, 3],
        [3, 5, 3, 7, 5],
        [1, 7, 5, 3, 5, 6],
        [6, 5, 5, 8, 3, 3, 3],
        [6, 8, 6, 8, 7, 3, 7, 5],
        [7, 9, 9, 1, 6, 8, 7, 5, 9],
        [2, 8, 2, 5, 5, 5, 2, 5, 7, 8],
        [1, 3, 5, 2, 4, 5, 3, 5, 1, 1, 6],
        [8, 6, 1, 1, 3, 4, 7, 5, 3, 6, 1, 9],
        [5, 8, 6, 6, 2, 6, 9, 3, 7, 4, 6, 9, 9],
        [3, 3, 5, 4, 4, 6, 9, 2, 5, 7, 7, 1, 6, 7],
        [8, 1, 4, 4, 6, 8, 4, 9, 7, 6, 1, 8, 4, 2, 9],
        [6, 5, 8, 6, 8, 3, 2, 4, 8, 8, 1, 5, 6, 8, 8, 7],
        [6, 3, 9, 1, 5, 6, 7, 7, 2, 2, 6, 2, 2, 1, 8, 8, 6],
        [4, 7, 8, 7, 5, 2, 8, 8, 2, 2, 7, 1, 3, 8, 1, 9, 4, 7],
        [1, 7, 8, 1, 4, 3, 8, 6, 6, 9, 6, 3, 5, 4, 7, 6, 4, 5, 6],
        [1, 1, 4, 9, 9, 8, 3, 3, 8, 1, 8, 1, 7, 6, 6, 3, 2, 1, 1, 6],
    )) == 139, "Veeery big pyramid"
    """