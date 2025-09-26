def first_and_last_element_swap(lst):
    lst[0], lst[-1] = lst[-1], lst[0]

    return lst


my_list = ['первый', 'второй', 'третий', 'четвертый', 'пятый']

print(first_and_last_element_swap(my_list))