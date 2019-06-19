def find_longest_palindrome_substring(str):

    if not str:
        return None
    #

    str_length = len(str)
    if str_length == 1:
        return str
    #

    sol = [ [0 for _ in range(str_length)] for _ in range(str_length)]

    # length-1 palindrome
    for i in range(str_length):
        sol[i][i] = 1
    #
    max_length, start = 1, 0

    # length-k(k>=2) palindrome
    for l in range(2, str_length+1):
        for i in range(str_length-l+1):
            if ((sol[i+1][i+l-2]==1) or (l==2)) and (str[i]==str[i+l-1]):
                sol[i][i+l-1] = 1
                max_length, start = l, i
            #
        #
    #
    # for i in range(str_length):
    #     print()
    #     for j in range(str_length):
    #         print(sol[i][j], end=' ')
    #     #
    # #
    # print()

    return str[start:(start+max_length)]
#


if __name__ == '__main__':

    print('Please input the string: ', end='')
    src = input() # hello xiao mi

    print('Result: ', end='')
    print(find_longest_palindrome_substring(src))
#