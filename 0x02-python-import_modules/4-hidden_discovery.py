#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    def_names = dir(hidden_4)
    for items in sorted(def_names):
        if not item.startswith("__"):
            print(items)
