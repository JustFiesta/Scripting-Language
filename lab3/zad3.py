from array import *
import random

array_len = int(input("Podaj wielkość tablicy: "))

usr_arr = array('i')

for i in range(array_len):
    rand = random.randrange(-5, 5)
    usr_arr.append(rand)

file_path = input("Podaj nazwę pliku dla listy: ")

usr_file = open(file_path, "a")

for value in usr_arr:
    usr_file.write(str(value) + " ")

print("Zapisano tablicę do pliku: ", file_path)