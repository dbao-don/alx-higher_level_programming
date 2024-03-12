#!/usr/bin/python3
for inner in range(0, 10):
    for outer in range(inner + 1, 10):
        if inner < 8:
            print('{}{}'.format(inner, outer), end=', ')
        else:
            print('{}{}'.format(inner, outer))
