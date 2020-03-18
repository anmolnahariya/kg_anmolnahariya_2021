from sys import argv

script, s1, s2 = argv

def str_map(a,b):
    if len(a) != len(b):
        print(False)
        exit(0)

    marked = [False] * 256 #256 ASCII codes
    char_map = [-1] * 256

    for i in range(len(a)):
        if char_map[ord(a[i])] == -1:
            if marked[ord(a[i])] == True:
                print(False)
                exit(0)

            marked[(ord(b[i]))] = True
            char_map[ord(a[i])] = b[i]

        elif char_map[ord(a[i])] != b[i]:
            print(False)
            exit(0)
    print(True)
    exit(0)

str_map(s1,s2)