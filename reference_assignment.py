x = 1
def fun1(x):
    print('id(x):{} at the top of func1'.format(id(x)))
    x = 2
    print('id(x):{}, id(2):{} after the assignment'.format(id(x), id(2)))
#
print('####### fun1 #######')
fun1(x)
print(x)        # 1


a = []
def fun2(a):
    print('id(a):{} at the top of func2'.format(id(a)))
    a.append(1)
    print('id(a):{} after the assignment'.format(id(a)))
#
print('####### fun2 #######')
fun2(a)
print(a)       # [1]


class PersonStr:
    name = 'aaa'
#
p1 = PersonStr()
p2 = PersonStr()
print('####### Member variable in Class PersonStr #######')
print('id(p1.name):{} before assignment, and value of p1.name:{}'.format(id(p1.name), p1.name))
p1.name = 'bbb'
print('id(p1.name):{} after assignment, and value of p1.name:{}'.format(id(p1.name), p1.name))
print('id(p2.name):{} and id(PersonStr.name):{} are unchanged'.format(id(p2.name), id(PersonStr.name)))



class PersonArr:
    name = []
#
p1 = PersonArr()
p2 = PersonArr()
print('####### Member variable in Class PersonArr #######')
print('id(p1.name):{} before append op, and value of p1.name:{}'.format(id(p1.name), p1.name))
p1.name.append(1)
print('id(p1.name):{} after append op, and value of p1.name:{}'.format(id(p1.name), p1.name))
print('id(p2.name):{} and id(PersonArr.name):{} are unchanged'.format(id(p2.name), id(PersonArr.name)))