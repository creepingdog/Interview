def change_making_DP(coin_values, amount):

    num_coins = [0]*(amount+1)
    coin_track = [1]*(amount+1)

    for a in range(1, amount + 1):
        min_num_coins = a  # 从第一个开始到money的所有情况初始
        v = min(coin_values)
        for value in coin_values:
            if value > a:
                break
            #
            temp = num_coins[a - value] + 1
            if temp < min_num_coins:
                min_num_coins = temp
                v = value
            #
        #
        num_coins[a] = min_num_coins
        coin_track[a] = v
    #
    return num_coins, coin_track
#


if __name__ == '__main__':
    coin_values = [1, 3, 5, 10, 25]
    amount = 63
    num_coins, coin_track = change_making_DP(coin_values, amount)
    # print(num_coins)
    # print(coin_track)
    print('Min # of coins to get amount {} is {}: '.format(amount, num_coins[-1]), end='')
    i = amount
    while i > 0:
        print(coin_track[i], end='')
        print(' => ', end='')
        i = i - coin_track[i]
    #
#
