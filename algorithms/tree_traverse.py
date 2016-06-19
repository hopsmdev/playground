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

    def is_leaf(self):
        return bool(self.children)


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

    def traverse(self, identifier, mode=_DEPTH):
        # Python generator. Loosly based on an algorithm from
        # 'Essential LISP' by John R. Anderson, Albert T. Corbett,
        # and Brian J. Reiser, page 239-241
        yield identifier
        queue = self[identifier].children
        while queue:
            yield queue[0]
            expansion = self[queue[0]].children
            if mode == _DEPTH:
                queue = expansion + queue[1:]  # depth-first
            elif mode == _BREADTH:
                queue = queue[1:] + expansion  # width-first

    def __getitem__(self, key):
        return self.__nodes[key]

    def __setitem__(self, key, item):
        self.__nodes[key] = item



def simple():
    tree = Tree()

    tree.add_node("Harry")  # root node
    tree.add_node("Jane", "Harry")
    tree.add_node("Bill", "Harry")
    tree.add_node("Joe", "Jane")
    tree.add_node("Diane", "Jane")
    tree.add_node("George", "Diane")
    tree.add_node("Mary", "Diane")
    tree.add_node("Jill", "George")
    tree.add_node("Carol", "Jill")
    tree.add_node("Grace", "Bill")
    tree.add_node("Mark", "Jane")

    tree.display("Harry")
    print("***** DEPTH-FIRST ITERATION *****")
    for node in tree.traverse("Harry"):
        print(node)
    print("***** BREADTH-FIRST ITERATION *****")
    for node in tree.traverse("Harry", mode=_BREADTH):
        print(node)



def test():
    """
    ((1,),
    (2, 3),
    (3, 3, 1),
    (3, 1, 5, 4),
    (3, 1, 3, 1, 3),
    (2, 2, 2, 2, 2, 2),
    (5, 6, 4, 5, 6, 4, 3))
    :return:
    """
    tree = Tree()
    tree.add_node((0,0))  # root node
    tree.add_node((1,0), (0,0))
    tree.add_node((1,1), (0,0))
    tree.add_node((2,0), (1,0))
    tree.add_node((2,1), (1,0))
    tree.add_node((2,1), (1,1))
    tree.add_node((2,2), (1,1))

    tree.display((0,0))
    print("***** DEPTH-FIRST ITERATION *****")
    for node in tree.traverse((0,0)):
        print(node)
    print("***** BREADTH-FIRST ITERATION *****")
    for node in tree.traverse((0,0), mode=_BREADTH):
        print(node)


if __name__ == "__main__":
    #simple()
    test()