def change_making_DP(coin_values, amount):

    num_coins = [0]*(amount+1)
    coin_track = [1]*(amount+1)

    for a in range(1, amount + 1):
        min_num_coins = 1e10  # 从第一个开始到money的所有情况初始
        v = min(coin_values)
        found_solution = False
        for value in coin_values:
            if value > a:
                break
            #
            if num_coins[a - value] == -1:
                continue
            #

            found_solution = True
            temp = num_coins[a - value] + 1
            if temp < min_num_coins:
                min_num_coins = temp
                v = value
            #
        #
        if found_solution:
            num_coins[a] = min_num_coins
            coin_track[a] = v
        else:
            num_coins[a] = -1
            coin_track[a] = None
        #
    #
    return num_coins, coin_track
#


if __name__ == '__main__':

    print('Please input the coin values separately by comma: ', end='')
    coin_values_str = input()
    coin_values = [int(cv.strip()) for cv in coin_values_str.split(',')]
    coin_values = sorted(coin_values)

    print('Please input the total amount: ', end='')
    amount = int(input())

    num_coins, coin_track = change_making_DP(coin_values, amount)

    # print(num_coins)
    # print(coin_track)

    print('Min # of coins to get amount {} is {}: '.format(amount, num_coins[-1]), end='')
    i = amount
    while i > 0:
        print(coin_track[i], end='')
        if not coin_track[i]:
            break
        #
        print(' => ', end='')
        i = i - coin_track[i]
    #
#
