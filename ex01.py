def only_ints(a, b):
    if type(a) is int:
        if type(b) is int:
            print('True')
        else:
            print('False')
    else:
        print('False')

only_ints('a', 9)
only_ints(6, 'a')
only_ints(1, 69)