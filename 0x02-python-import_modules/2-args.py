#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_list = sys.argv
    len_args = len(args_list)
    idx = 1
    if len_args >= 2:
        if len_args == 2:
            print('{} argument:'.format(len_args - 1))
        else:
            print('{} arguments:'.format(len_args - 1))
        for args in range(len_args - 1):
            print('{}: {}'.format(idx, args_list[idx]))
            idx += 1
    else:
        print('0 arguments.')
