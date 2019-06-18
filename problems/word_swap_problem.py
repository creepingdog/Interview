def swap_words(char_arr):
    def swap(start, end):
        while start < end:
            char_arr[start], char_arr[end] = char_arr[end], char_arr[start]
            start += 1
            end -= 1
        #
    #

    length = len(char_arr)
    swap(0, length-1)

    p1 = 0
    p2 = 0
    while p2 < length:
        if char_arr[p2] == ' ':
            swap(p1, p2-1)
            p1 = p2 + 1
        #
        p2 += 1
    #
    swap(p1, length-1)
#
#
#
# def swap(chars, start, end):
#
#     p1 = start
#     p2 = end
#
#     while p1 < p2:
#         chars[p1], chars[p2] = chars[p2], chars[p1]
#         print(chars)
#         if chars[p1] == ' ':
#             swap(chars, start, p1-1)
#             start = p1 + 1
#         if chars[p2] == ' ':
#             swap(chars, p2+1, end)
#             end = p2 - 1
#         #
#         p1 += 1
#         p2 -= 1
#     #
#     return start, end
# #


if __name__ == '__main__':

    print('Please input the string: ', end='')
    src = input() # hello xiao mi

    char_arr = list(src)
    swap_words(char_arr)
    print('Result: ', end='')
    print(''.join(char_arr))
#
