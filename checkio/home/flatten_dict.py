"""
Python dictionaries are a convenient data type to store and process
configurations. They allow you to store data by keys to create nested structures
You are given a dictionary where the keys are strings and the values are strings
or dictionaries. The goal is flatten the dictionary, but save the structures in
the keys. The result should be the a dictionary without the nested dictionaries
The keys should contain paths that contain the parent keys from the original
dictionary. The keys in the path are separated by a "/".
If a value is an empty dictionary, then it should be replaced by an empty
string (""). Let's look at an example:

{
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}
    }
}

The result will be:

{"name/first": "One",           #one parent
 "name/last": "Drone",
 "job": "scout",                #root key
 "recent": "",                  #empty dict
 "additional/place/zone": "1",  #third level
 "additional/place/cell": "2"}
"""


def flatten(dictionary):
    print("-----> ", dictionary)
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        print(path, current)
        if isinstance(current, dict):
            for k, v in current.items():
                print('\t', k, v)
                if isinstance(v, dict):
                    if v:
                        stack.append((path + (k,), v))
                        print('\t\t', stack)
                    else:
                        result["/".join((path + (k,)))] = ""
                else:
                    print('here')
                    result["/".join((path + (k,)))] = v
                    print("\t\t\t", result)

    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}