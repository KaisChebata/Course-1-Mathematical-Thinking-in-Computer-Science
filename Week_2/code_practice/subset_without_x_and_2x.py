"""
Problem: Subset without x and 2x
---------------------------------
Select the maximum number of integers among 1..50 with no x and 2x simultaneously.

on other words,
what is the Maximal number of integers among 1..50 
that can be selected if we are not allowed to select n and 2n at at same time.
"""
import copy

def maximum_number_of_ints_in_set(lst_of_numbers):
    valid_counter = 0
    lst_length = len(lst_of_numbers)
    valid_list = copy.copy(lst_of_numbers)
    for i in range(lst_length):
        for j in range(i + 1, lst_length):
            if lst_of_numbers[i] == (lst_of_numbers[j] / 2):
                valid_list.pop(j)
                valid_counter += 1
                
    return valid_counter, valid_list


numbers_list = [x for x in range(1, 51)]
ten_element_test_list = [y for y in range(1, 11)]
print(numbers_list)
max_num = maximum_number_of_ints_in_set(ten_element_test_list)
print(max_num)