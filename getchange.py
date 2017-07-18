"""
Module to calculate change.
"""

import collections


coin_names = ['quarters', 'dimes', 'nickels', 'pennies']
coin_values = [25, 10, 5, 1]
coins = collections.OrderedDict(zip(coin_names, coin_values)))

dollar_names = ['twenties', 'tens', 'fives', 'ones']
dollar_values = [20, 10, 5, 1]
dollars = collections.OrderedDict(zip(dollar_names, dollar_values))


def get_coins(change):
    """
    Return a dictionary of coin_name:coin_count needed to give
    change for coins.

    The variable change should be an integer.
    To get coins for .35 dollars, call get_coins(35).
    """
    coin_counts = {
        'quarters':0,
        'dimes':0,
        'nickels':0,
        'pennies':0
        }
    for coin in coins:
        (coin_count, new_change) = divmod(change, coins[coin])
        coin_counts[coin] = coin_count
        change = new_change
    return coin_counts


def get_dollars(change):
    """
    Return a dictionary of coin_name:coin_count needed to give
    change for coins.

    The variable change should be an integer.
    To get coins for .35 dollars, call get_coins(35).
    """
    dollar_counts = {
        'twenties':0,
        'tens':0,
        'fives':0,
        'ones':0
        }
    for dollar in dollars:
        (dollar_count, new_change) = divmod(change, dollars[dollar])
        dollar_counts[coin] = dollar_count
        change = new_change
    return dollar_counts


def find_change(cost, given):
    """
    Return tuple (dollars, cents) representing change owed.
    """
    raw_change = int((given - cost) * 100)
    return divmod(raw_change, 100)


def print_coin_change(coin_dict):
    """
    Print out coin names and amounts.

    Expects a dictionary from get_coins.
    """
    change_str = (
        'Quarters: {quarters}\n'
        'Dimes: {dimes}\n'
        'Nickels: {nickels}\n'
        'Pennies: {pennies}'
        )
    print(change_str.format(**coin_dict))


def print_dollar_change(dollar_dict):
    """
    Print out dollar names and amounts.

    Expects a dictionary from get_dollars.
    """
    change_str = (
        'Twenties: {twenties}\n'
        'Tens: {tens}\n'
        'Fives: {fives}\n'
        'Ones: {ones}'
        )
    print(change_str.format(**dollar_dict))


def calc_and_print_change(cost, given):
    dollars, cents = find_change(cost, given)

    coin_count_dict = get_coins(cents)
    dollar_count_dict = get_dollars(dollars)

    print('Your change is {}.{}'.format(dollars, cents))
    print_dollar_change(dollar_count_dict)
    print_coin_change(coin_count_dict)


def main():
    cost = input('How much does customer owe? ')
    given = input('How much did customer give? ')
    calc_and_print_change(cost, given)


if __name__ == '__main__':
    main()
