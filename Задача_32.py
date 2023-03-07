# Задача 32:
#     Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#     (т.е. не меньше заданного минимума и не больше заданного максимума)


def find_index(some_list, from_index, to_index):
    """
    :param some_list: список в котором нужно найти индексы элементов из указанного диапазона
    :param from_index: индекс, с которого начинается диапазон
    :param to_index: индекс, которым заканчивается диапазон
    :return: словарь {'index': value}
    """
    dict_range = {}
    for i in range(from_index, to_index):
        dict_range[i] = some_list[i]
    return dict_range


list_x = input("Введите элементы списка через пробел: ").split()
list_x = [int(i) for i in list_x]
start_x_i = list_x.index(int(input("Введите элемент, из списка, начиная с которого нужно найти индексы: ")))
end_x_i = list_x.index(int(input("Введите элемент, до которого(включительно) нужно найти индексы: ")))

print("Словарь {индекс: значение}:", find_index(list_x, start_x_i, end_x_i))
