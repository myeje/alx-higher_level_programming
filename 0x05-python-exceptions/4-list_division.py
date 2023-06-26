#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    divide = 0
    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                divide = my_list_1[i] / my_list_2[i]
            else:
                raise TypeError
        except TypeError:
            divide = 0
            print("wrong type")
        except ZeroDivisionError:
            divide = 0
            print("division by 0")
        except IndexError:
            divide = 0
            print("out of range")
        finally:
            new_list.append(divide)
    return (new_list)
