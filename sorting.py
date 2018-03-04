def bubble_sort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(0, n-i-1):
            if alist[j] > alist[j+1]:
                alist[j+1], alist[j] = alist[j], alist[j+1]
            #
        #
    #
    return alist
#

alist = [1,5,2,6,9,3]
print(bubble_sort(alist))