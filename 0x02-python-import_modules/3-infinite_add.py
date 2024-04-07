#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_list = sys.argv
    len_args = len(args_list)
    sum_args = 0
    idx = 1
    for args in range(len_args - 1):
        sum_args += int(args_list[idx])
        idx += 1
    print(sum_args)
