def first_and_last_element_swap(lst):
    lst.insert(0, my_list[-1])

    lst.append(my_list[1])

    lst.pop(1)

    lst.pop(-2)

    return lst


my_list = ['первый', 'второй', 'третий', 'четвертый', 'пятый']

print(first_and_last_element_swap(my_list))