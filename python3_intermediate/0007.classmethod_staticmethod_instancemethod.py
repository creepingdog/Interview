class InstanceRegistry(object):

    # private class variable
    __number = 0

    @classmethod
    def register(cls):
        cls.__number += 1

    @classmethod
    def get_count(cls):
        print('[{}::get_count]'.format(cls.__class__))
        return cls.__number

    @staticmethod
    def calc_sum(*nums):
        print('[InstanceRegistry::calc_sum()]')
        return sum(nums)

    @staticmethod
    def calc_avg(*nums):
        print('[InstanceRegistry::calc_avg()]')
        return InstanceRegistry.calc_sum(*nums)/len(nums)

    def __new__(cls):
        cls.register()
        return super().__new__(cls)


class SubInstanceRegistry(InstanceRegistry):
    __number = 0

    # @classmethod
    # def get_count(cls):
    #     print('[SubInstanceRegistry::get_count]')
    #     return cls.__number

    @staticmethod
    def calc_avg(*nums):
        print('[SubInstanceRegistry::calc_avg()]')
        return sum(nums) / len(nums)


class Registry:
    __number = 0

    @classmethod
    def get_count(cls):
        print('[{}::get_count]'.format(cls.__class__))
        return cls.__number


    @staticmethod
    def get_count():
        print('[Registry::get_count] This is StaticMethod')
        return Registry.__number
#

if __name__ == '__main__':
    sir = SubInstanceRegistry()
    print('\nResult of sir.calc_avg(24, 26). StaticMethod overridden in SubInstanceRegistry')
    print(sir.calc_avg(24, 26))
    print('\nResult of sir.calc_sum(24, 26). StaticMethod not implemented in SubInstanceRegistry so the one in InstanceRegistry gets called')
    print(sir.calc_sum(24, 26))

    print('\nResult of sir.get_count(). ClassMethod figures out inheritance well')
    print(sir.get_count())
    print(SubInstanceRegistry.get_count())

    print('\nCounter in InstanceRegistry works well. Even for the SubInstanceRegistry instances')
    ir1 = InstanceRegistry()
    ir2 = InstanceRegistry()
    sir2 = SubInstanceRegistry()
    print(InstanceRegistry.get_count())

    print('\nSame names on ClassMethod and StaticMethod, ClassMethod is overridden')
    r1 = Registry()
    r2 = Registry()
    print(Registry.get_count())
#