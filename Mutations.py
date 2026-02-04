def mutate_string(string, position, character):
    altered_string = ""
    for i in range(len(string)):
        if i == position:
            altered_string += character
            continue
        altered_string += string[i];
    return altered_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)