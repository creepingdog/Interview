def func(a=[]):
    a.append(1)
    return a
#

print(func())
print(func())

print(func.__name__)
print(func.__code__)
print(func.__defaults__)

func.__defaults__[0][:] = []
print(func())