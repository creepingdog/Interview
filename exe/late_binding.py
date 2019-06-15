# Actually the difference shown below involves several concepts:
# 1. Closure
# 2. Generator
# 3. Late binding


def create_multipliers_list():
    return [lambda x: i * x for i in range(5)]
#


def create_multipliers_tuple():
    return (lambda x: i * x for i in range(5))
#


if __name__ == '__main__':
    print('===== create_multipliers_list =====')
    for multiplier in create_multipliers_list():
        print(multiplier(2))
    #

    print()

    print('===== create_multipliers_tuple =====')
    for multiplier in create_multipliers_tuple():
        print(multiplier(2))
    #
#
