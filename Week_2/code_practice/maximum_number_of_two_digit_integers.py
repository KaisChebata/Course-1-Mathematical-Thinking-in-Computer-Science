"""
Problem: Maximum Number of Two-digit Integers.

There are 90 cards with all two-digit numbers on them:

10,11,12,...,19,20,21,...,90,91,...,99.

A player takes some of these cards. 
For each card taken she gets $1. 
However, if the player takes two cards that add up to 100 (say, 23 and 77), 
at the same time, she loses all the money. 
How much could she get? 

In mathematical language: 
(what is the maximum number of elements in a subset of {10,12,...,99} 
that does not contain any two numbers x and y with x+y =100 ?) 
"""

import copy

"""here in this function max_two_digit_integers(card_list) 
we iterate through the list and modify the counter 
of the elements number during the comparsion. 
if match the condition we decrease the counter.
then returning the value of the counter."""

# def max_two_digit_integers(card_list):
#     num_of_cards = len(card_list)
#     for i in range(len(card_list)):
#         for j in range(i + 1, len(card_list)):
#             if card_list[i] + card_list[j] == 100:
#                 num_of_cards -= 1
#     return num_of_cards


def max_number_of_elements_in_subset(num_list):
    """(lst) -> lst, int
    here we'll return the valid subset lst of (num_list) 
    that contains 90 elements [10,11,12,...,19,20,21,...,90,91,...,99], 
    and the maximum number of elements in a subset of (num_list) 
    that does not contain any two numbers x and y with x+y =100.

    >>> max_number_of_elements_in_subset([10,11,12,...,19,20,21,...,90,91,...,99])
    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 
    32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 
    43, 44, 45, 46, 47, 48, 49, 50, 91, 92, 93, 
    94, 95, 96, 97, 98, 99] - where this the valid subset (lst)
    
    50 - where this is the max number of elements in the valid subset.
    """
    valid_list = copy.copy(num_list)

    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] == 100:
                valid_list.pop(j)
    
    return valid_list, len(valid_list)


print('---------------------------------------------')
card_list = [x for x in range(10, 100)]

print(card_list, len(card_list))

subset, max_elements_num = max_number_of_elements_in_subset(card_list)
print('the valid subset: ')
print(subset)
print('max_elements_num: ', max_elements_num)
