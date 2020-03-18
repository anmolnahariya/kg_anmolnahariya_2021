from sys import argv

script, s1, s2 = argv

def str_map(a,b):
    if len(a) != len(b):
        print(False)
        exit(0)

    marked = [False] * 256 #256 ASCII codes
    char_map = [-1] * 256