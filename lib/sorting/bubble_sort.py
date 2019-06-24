import copy


def bubble_sort(l, inplace=False):
    if not inplace:
        l = copy.deepcopy(l)
    #
    n = len(l)
    while n>1:
        p = 0
        for i in range(1, n):
            if l[i-1] > l[i]:
                l[i-1], l[i] = l[i], l[i-1]
                p = i
            #
        #
        n = p
    #
    return l
#



if __name__ == '__main__':

    print('Please input the numbers separated by comma: ', end='')
    src = input()

    l = [int(x.strip()) for x in src.split(',')]
    bubble_sort(l, inplace=True)
    print('Result: ', end='')
    print(l)
#