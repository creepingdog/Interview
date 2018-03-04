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

ObjectCreatorMirror2 = type('ObjectCreator', (), {})
print(ObjectCreatorMirror2)

ObjectCreatorChild = type('ObjectCreatorChild', (ObjectCreator,), {})
print(ObjectCreatorChild)
print(ObjectCreatorChild.new_attribute)


def echo_new_attribute(self):
    print(self.new_attribute)
#

ObjectCreatorChild = type('ObjectCreatorChild', (ObjectCreator,), {'echo_new_attribute': echo_new_attribute})
print(hasattr(ObjectCreator, 'echo_new_attribute'))
print(hasattr(ObjectCreatorChild, 'echo_new_attribute'))

obj_creator_child = ObjectCreatorChild()
obj_creator_child.echo_new_attribute()

