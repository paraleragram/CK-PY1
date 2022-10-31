def get_count_char(str_):
    str_ = ''.join(str_.lower().split())
    freq = {}
    DEFAULT_COUNT = 0

    for symbol in str_:
        if symbol.isalpha():
            freq[symbol] = freq.get(symbol, DEFAULT_COUNT) + 1
    return freq


main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
print(get_count_char(main_str))

def get_percent_char(dict_):
    total_sum = sum(dict_.values())
    for symbol in dict_:
        dict_[symbol] = dict_[symbol] / total_sum * 100
    return dict_

print(get_percent_char(get_count_char(main_str)))
