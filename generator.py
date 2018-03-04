L = [x*x for x in range(10)]
print(L)        #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


g = (x*x for x in range(10))
print(g)        #<generator object <genexpr> at 0x00000233E71AEE08>