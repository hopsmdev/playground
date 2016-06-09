"""
We have an array of straight connections between drones.
Each connection is represented as a string with two names of friends
separated by hyphen. For example: "dr101-mr99" means what the
dr101 and mr99 are friends. Your should write a function that allow determine
more complex connection between drones. You are given two names also.
Try to determine if they are related through common bonds by any depth.
For example: if two drones have a common friends or friends who have common f
riends and so on.

Input: Three arguments: Information about friends as a tuple of strings;
first name as a string; second name as a string.

Output: Are these drones related or not as a boolean.

Example:

check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3") == True
check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout") == False

"""

from collections import defaultdict


def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath:
                    return newpath
        return None


def check_connection(network, first, second):

    connection_map = defaultdict(list)
    for connection in network:
        _first, _second = tuple(connection.split('-'))

        connection_map[_first].append(_second)
        connection_map[_second].append(_first)

    return bool(find_path(connection_map, first, second))


if __name__ == '__main__':


    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."



