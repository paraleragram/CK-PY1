from random import randint

def get_unique_list_numbers() -> list[int]:
    list_num = []
    start, end = -10, 10
    for i in range(15):
        num = randint(start, end)
        if num not in list_num:
            list_num.append(num)
    return list_num

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
