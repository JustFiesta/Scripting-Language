def histogram(path):
    with open(path, 'r') as file:
        histogram_dict = {}

        text = file.read()

        for char in text:
            if char in histogram_dict:
                histogram_dict[char] += 1
            else:
                histogram_dict[char] = 1
    return histogram_dict


path_to_file = 'test.txt'
result = histogram(path_to_file)
print(result)