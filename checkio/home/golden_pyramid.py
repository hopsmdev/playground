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
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def test(pyramid):
    """
    ((1,),
    (2, 3),
    (3, 3, 1),
    (3, 1, 5, 4),
    (3, 1, 3, 1, 3),
    :return:
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
    #test(pyramid)

    root_row_idx, root_col_idx = 0, 0
    root = (root_row_idx, root_col_idx)
    tree = Tree(pyramid)
    tree.add_node((0, 0))  # root node

    for row_idx, row in enumerate(pyramid[1:]):
        for col_idx, col in enumerate(row):
            if col_idx == root_col_idx:
                tree.add_node((row_idx, col_idx), root)
        root = (row_idx, col_idx)



if __name__ == '__main__':
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
