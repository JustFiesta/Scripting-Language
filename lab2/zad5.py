def sum_array(array):
    sum = 0

    for num in array:
        sum = sum + num

    return sum

def print_sum_array(file, sum_func):
    try:
        with open(file, 'r') as plik:
            liczby = [float(line.strip()) for line in plik]
            suma = sum_func(liczby)
            return suma
    except FileNotFoundError:
        print(f"Plik o nazwie {file} nie został znaleziony.")
        return None
    except ValueError:
        print("Błąd: W pliku znajduje się coś innego niż liczby.")
        return None


# Przykładowe użycie
lista_liczb = [1, 2, 3, 4, 5]
suma_z_listy = sum_array(lista_liczb)
print("Suma z listy:", suma_z_listy)

file = "nums.txt"
suma_z_pliku = print_sum_array(file, sum_array)

if suma_z_pliku is not None:
    print(f"Suma z pliku {file}: {suma_z_pliku}")