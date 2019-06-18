def remove_common_chars(s1, s2):
    if not s1 or not s2:
        return s1
    #

    hash_table = [0] * 256
    # build hash_table for the chars in s2
    for c in list(s2):
        hash_table[ord(c)] += 1
    #

    char_arr = list(s1)
    p1 = 0
    p2 = 0
    while p1 < len(s1):
        char_arr[p2] = char_arr[p1]
        c = char_arr[p1]
        if hash_table[ord(c)] == 0:
            p1 += 1
            p2 += 1
        else:
            p1 += 1
        #
    #
    return ''.join(char_arr[:p2])
#


if __name__ == '__main__':

    print('Please input the source string: ', end='')
    src = input() # They are students.

    print('Please input the string to be removed: ', end='')
    rem = input() # aeiou

    print('Result string after removal: ', end='')
    print(remove_common_chars(src, rem))
#
