#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    lt = []
    for x in range(list_length):

        try:
            lt.append(my_list_1[x] / my_list_2[x])
            continue
        except ZeroDivisionError:
            lt.append(0)
            print("division by 0")
        except TypeError:
            lt.append(0)
            print("Wrong type")
        except IndexError:
            lt.append(0)
            print("Out of range")
        finally:
            pass
    return lt
