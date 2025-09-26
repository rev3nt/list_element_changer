def first_and_last_element_swap(lst):

    first_element = lst[0]

    last_element = lst[-1]

    lst[0] = last_element

    lst[-1] = first_element

    return lst


my_list = ['первый', 'второй', 'третий', 'четвертый', 'пятый']

print(first_and_last_element_swap(my_list))