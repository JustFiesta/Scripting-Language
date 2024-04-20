import numpy as np

def create_square_array():
    array = np.zeros((5, 5), dtype=int)

    array[0] = [2, 3, 4, 5, 6]

    for i in range(1, 5):
        for j in range(5):
            array[i, j] = array[i-1, j] ** 2

    return array

result = create_square_array()
print(result)
