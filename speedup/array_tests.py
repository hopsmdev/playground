import ctypes

from array import array

from utils.execution_time import execution_time

TEST_LOOPS=100
VERBOSE=False

class _ArrayIterator(object):
    def __init__(self, array):
        self._array = array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array):
            entry = self._array[self._cur_index]
            self._cur_index += 1
            return entry
        raise StopIteration


class Array(object):
    def __init__(self, size):
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def clear(self, value):
        for i in range(self._size):
            self._elements[i] = value

    def __len__(self):
        return self._size

    def __getitem__(self, item):
        return self._elements[item]

    def __setitem__(self, key, value):
        self._elements[key] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

    def __str__(self):
        return str(self._elements)


@execution_time(loops=TEST_LOOPS, verbose=VERBOSE)
def test_fill_int_array_from_arrays():
    ints = array('i', (1 for i in range(100000)))

@execution_time(loops=TEST_LOOPS, verbose=VERBOSE)
def test_fill_int_array():
    ArrayType = ctypes.c_int * 100000
    slots = ArrayType()
    for i in range(100000):
        slots[1] = 1

@execution_time(loops=TEST_LOOPS, verbose=VERBOSE)
def test_fill_array():
    a = Array(100000)
    a.clear(1)

@execution_time(loops=TEST_LOOPS, verbose=VERBOSE)
def test_fill_list():
    l = [1] * 100000

@execution_time(loops=TEST_LOOPS, verbose=VERBOSE)
def test_fill_tuple():
    t = (1,) * 100000


def test_size():
    import sys

    ints = array('i', (1 for i in range(100000)))
    print("insts: ", sys.getsizeof(ints))
    print("ints: ", type(ints))

    ArrayType = ctypes.c_int * 100000
    slots = ArrayType()
    for i in range(100000):
        slots[i] = 1
    print("c_int: ", sys.getsizeof(slots))
    print("c_int: ", type(slots))

    a = Array(100000)
    a.clear(1)
    print("Array: ", len(a))
    print("Array: ", sys.getsizeof(a))
    print("Array: ", type(a))


    l = [1] * 100000
    print("List: ", sys.getsizeof(l))

    t = (1,) * 100000
    print("Tuple: ", sys.getsizeof(t))


test_fill_int_array()
test_fill_array()
test_fill_list()
test_fill_tuple()

test_size()