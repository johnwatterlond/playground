

import collections


coin_tuples = [('quarters', 25), ('dimes', 10), ('nickels', 5), ('pennies', 1)]
coin_vals = collections.OrderedDict(coin_tuples)


def get_coins(change):
    """
    Return a dictionary of coin_name:coin_count needed to give change for coins.
    """
    coin_counts = {'quarters':0, 'dimes':0, 'nickels':0, 'pennies':0}
    for coin in coin_vals:
        (num, new_change) = divmod(change, coin_vals[coin])
        coin_counts[coin] = num
        change = new_change
    return coin_counts


def find_change(cost, given):
    """
    Return tuple (dollars, cents) representing change owed.
    """
    raw_change = int((given - cost) * 100)
    return divmod(raw_change, 100)


def calc_and_print_change(cost, given):
    dollars, cents = find_change(cost, given)
    coin_count_dict = get_coins(cents)
    print('Dollars: {}'.format(dollars))
    print_coin_change(coin_count_dict)


def print_coin_change(coin_dict):
    change_str = 'Quarters: {quarters}\nDimes: {dimes}\nNickels: {nickels}\nPennies: {pennies}'
    print(change_str.format(**coin_dict))




#TODO:
# output should be:
# Your change is: blablalba.blablal
# That is:
# twenties: bla
# tens: bla
# fives: bla
# ones: bla
# print_coin_change...
