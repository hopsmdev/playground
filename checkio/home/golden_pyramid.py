_ROOT, _DEPTH, _BREADTH = range(3)


class Node:
    def __init__(self, identifier, value):
        self.__identifier = identifier
        self.__children = []
        self.__value = value

    @property
    def identifier(self):
        return self.__identifier

    @property
    def children(self):
        return self.__children

    @property
    def value(self):
        return self.__value

    def add_child(self, identifier):
        self.__children.append(identifier)

    def is_leaf(self):
        return bool(self.children)

    def __str__(self):
        return str(self.identifier)

    def __repr__(self):
        return str(self.identifier)


class Tree:

    def __init__(self, pyramid):
        self.__nodes = {}
        self.pyramid = pyramid

    @property
    def nodes(self):
        return self.__nodes

    def add_node(self, identifier, parent=None):
        node = Node(identifier,
                    self.pyramid[identifier[0]][identifier[1]])
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


def test(pyramid):
    """
    ((1,),
    (2, 3),
    (3, 3, 1),
    (3, 1, 5, 4),
    """

    tree = Tree(pyramid)
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
            values.append([tree[node].value for node in path])

        max_gold_path = [sum(path) for path in values]
        max_gold.append(max(max_gold_path))
        print(paths)
        print(values)
        print(max_gold_path)
        print("MAX GOLD", max(max_gold))


def count_gold(pyramid):

    root_row_idx, root_col_idx = 0, 0
    root = (root_row_idx, root_col_idx)

    # create Tree with root (0, 0)
    tree = Tree(pyramid)
    tree.add_node(root)  # root node

    # list of roots: [((0,0)), ((1,0), (1,1), (1, 2)) ,,,((n, n+1),(n, n+2))]
    root_col_idxs = [(row_idx, range(len(row)))
                     for row_idx, row in enumerate(pyramid[:-1])]

    for row_idx, col_idxs in root_col_idxs:  # iterate over list of roots
        for col_idx in col_idxs:
            root = (row_idx, col_idx)

            # find children nodes
            next_row = min(row_idx + 1, len(pyramid) - 1)
            next_col = min(col_idx + 1, next_row)

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
        paths = find_all_paths(tree, (0,0), endpoint)
        print(endpoint, paths)

        # translate node coordinates to node value (values list)
        # for example from (0, 0) to 1
        values = []
        for path in paths:
            values.append([tree[node].value for node in path])

        print(values)

        # sum all values for given path
        max_gold_path = [sum(path) for path in values]
        print(max_gold_path)

        # add maximum value for path to max_gold list
        max_gold.append(max(max_gold_path))

    print("MAX GOLD", max(max_gold))
    return max(max_gold)


if __name__ == '__main__':
    """
    test((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4)))
    """
    #These "asserts" using only for self-checking and not necessary for auto-testing
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
