list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_el = max(list_numbers)

for i in range(len(list_numbers)):
    if max_el == list_numbers[i]:
        index = i
        break

list_numbers[index], list_numbers[-1] = list_numbers[-1], list_numbers[index]
print(list_numbers)
