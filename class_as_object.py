class ObjectCreator(object):
    pass
#

def echo(o):
    print(o)

my_object = ObjectCreator()
print(my_object)

print(ObjectCreator)
echo(ObjectCreator)
print(hasattr(ObjectCreator, 'new_attribute'))
ObjectCreator.new_attribute = 'foo'
print(hasattr(ObjectCreator, 'new_attribute'))
print(ObjectCreator.new_attribute)
ObjectCreatorMirror = ObjectCreator
print(ObjectCreatorMirror)
print(ObjectCreatorMirror.new_attribute)
print(ObjectCreatorMirror())
