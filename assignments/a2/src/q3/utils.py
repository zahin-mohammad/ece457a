import numpy as np

# l = np.fromstring('11 2 3 4', dtype=int, sep=' ')
# print(l)

np_arr = np.array([])


def serialize(l):
    assert (type(l) == type(np_arr)
            ), 'Trying to serialize a non-np.array type'

    return ' '.join(map(str, l))


def deserialize(s):
    assert(isinstance(s, str)), 'Trying to deserialize a non-str type'
    return np.fromstring(s, dtype=int, sep=' ')
