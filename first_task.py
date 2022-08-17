

def is_even(number):
    even_lst = str([0, 2, 4, 6, 8])
    my_number = list(str(number))
    if len(my_number) == 1 and my_number[0] in even_lst:
        return True
    elif len(my_number) > 1 and my_number[-1] in even_lst:
        return True
    else:
        return False

print(is_even(input()))

# Плюсы: данная функция работает со всеми типами данных
# Минусы: занимает много места,
