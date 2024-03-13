import random as random;

def lotto():
    array = []
    i = 6

    while(i > 0):
        random_num = random.randint(1, 49)
        if not random_num in array:
            array.append(random_num)
            i = i-1
    return array

print(lotto())