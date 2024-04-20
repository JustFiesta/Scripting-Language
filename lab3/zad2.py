from array import *

array_len = int(input("Podaj wielkość tablicy: "))

usr_arr = array('i')

for i in range(array_len):
    usr_in = int(input("Podaj liczbę do tabeli: "))
    usr_arr.append(usr_in)

usr_arr = usr_arr[::-1]
print("Twoja tablica: ", usr_arr)