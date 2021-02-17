# this a python program to generate 2D array 
# col_num, row_num
def two_d_array(rows_num, cols_num):
    """(int, int) -> lst

    Return 2D array using col_num and row_num to create lst 
    with col_num as heigh and row_num as width, we'll initialize 
    the 2D with zeros(0's)

    >>> two_d_array(3, 3)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    """

    matrix = []

    for _ in range(rows_num):
        row = []
        for _ in range(cols_num):
            row.append(0)
        matrix.append(row)
    
    return matrix

mat = two_d_array(4, 4)

print('displaying mat as list of lists: \n', mat)
print('-----------------------------------')

print('\ndisplaying mat as a matrix form: ')
for i in range(len(mat)):
    print(mat[i])
print('-----------------------------------')

print('modifying matrix - mat[0][1] = 1')
mat[0][1] = 1

print(mat)
mat[0][1] = 0

print('-----------------------------------')

print('Modfying diagonal of the matrix: ')

for i in range(len(mat)):
    mat[i][i] = 1

print('Printing matrix after modifying its diagonal: ')

for row in range(len(mat)):
    print(mat[row])


mtx = []
for i in range(5):
    mtx.append([])
    for j in range(5):
        mtx[i].append(2)
print(mtx)

import copy
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

print('old_list: ', old_list)
print('Id of old_list: ', id(old_list))
print('new_list: ', new_list)
print('Id of new_list: ', id(new_list))
print('Checking if old_list and new_list are has same reference\
    (old_list is new_list)', old_list is new_list)
print('---------------------------------------------------------')

old_list = old_list = ['a', [1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)
print('adding new new object to old_list')
old_list.append([10, 11, 12])
print('old_list: ', old_list)
print('Id of old_list: ', id(old_list))
print('new_list: ', new_list)
print('Id of new_list: ', id(new_list))
print('remove an item at index = 0 of new_list')
new_list.pop(0)
print('new_list: ', new_list)
print('remove an object [1, 2, 3] from new_list: ')
new_list.remove([1, 2, 3])
print('new_list: ', new_list)
print('old_list: ', old_list)
print('--------------------------')
print('some tests on creating list, starting from 50 and ends with 99\
    with computing its length')
test_lst = [x for x in range(50, 100)]
print('test_lst: ', test_lst)
print('length of test_lst is: ', len(test_lst))

# -----------------------------------------------------------------------

num = 2.71828
print(round(num,2))

def round_the_float(num):
    num = round(num, 2)
    return num

a = 2.71828
a = round_the_float(a)
# b = a
#What is b's value when this line is reached? 
# print('#1 - b = ', b)

a = 2.71828
round_the_float(a)
b = a
print('#2 - b = ', b)
#What is b's value when this line is reached?

def absolute_reciprocal(an_int):
    abs(an_int)
    an_int = 1 / an_int
    return an_int

print(absolute_reciprocal(-5))

def find_the_odds(a_list):
    list_of_odds = []
    for i in range(len(a_list)):
        if i % 2 == 1:
            list_of_odds.append(a_list[i])
    return list_of_odds

my_list = [1, 5, 4, 4, 2, 1, 5, 9]
my_list = find_the_odds(my_list)
print(my_list)

def add_a_capitol(a_dict, a_state, a_city):
    a_dict[a_state] = a_city

my_capitols = {"Georgia": "Atlanta", "Idaho": "Boise", "Maine": "Augusta"}
add_a_capitol(my_capitols, 'Texas', 'Austin')
print(my_capitols)

# def dict_test(a_dict, a_char, a_new_char):
#     a_dict = {a_char: a_new_char}

# my_dict = {'a': 'A', 'b': 'B', 'c': 'C'}
# dict_test(my_dict, 'hi', 'bye')
# print(my_dict)
a = 5
b = a
b += 5
c = a
c *= 2
a -= 5
print(f'a: {a} - b:{b}')

list_1 = ["Bananas", "Apples", "Carrots"]
list_2 = list_1
print(f'list_1: {list_1}\nlist_2:{list_2}')
list_1.sort()
print(f'list_1: {list_1}\nlist_2:{list_2}')
list_2.append("Dewberry")
print(f'list_1: {list_1}\nlist_2:{list_2}')
list_2.reverse()
print(f'list_1: {list_1}\nlist_2:{list_2}')

a = {}
a = {1: "Face", 2: "Beans", 3: "Pants", 4: "Loaf"}
b = a
a[5] = "Straw"
b[4] = "Geese"
a[4] = "Couch"
b[6] = "Trot"
print(a[6])

a = "I got"
a += " a "
print(a)
b = a
print(a, b)
b += "feeling"
print(a, b)
a = a.upper()
print(a)
print(b)

# implementing an iterative factorial procedure
def fact_iter(num):
    assert num > 0
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(fact_iter(5))

# implementing recursive factorial procedure
def fact_recursive(num):
    assert num > 0
    if num == 1:
        return 1
    else:
        return num * fact_recursive(num - 1)

print(fact_recursive(5))


# prove that monetaty amount starting from 8 can be 
# paid using coins of denominations 3 and 5.
def change(amount):
    assert amount >= 8

    if amount == 8:
        return [3, 5]
    if amount == 9:
        return [3, 3, 3]
    if amount == 10:
        return [5, 5]
    
    coins = change(amount - 3)
    coins.append(3)

    return coins

# Develop a Python method change(amount) that for any integer amount 
# in the range from 24 to 1000 returns a list consisting of numbers 5 and 7 only, 
# such that their sum is equal to amount. 
# For example, change(28) may return [7, 7, 7, 7], 
# while change(49) may return [7, 7, 7, 7, 7, 7, 7] or 
# [5, 5, 5, 5, 5, 5, 5, 7, 7] or [7, 5, 5, 5, 5, 5, 5, 5, 7].

# To solve this quiz, implement the method change(amount) on your machine, 
# test it on several inputs, 
# and then paste your code in the field below and press the submit quiz button. 
# Your submission should contain the change method only 
# (in particular, make sure to remove all print statements).

def change_5_7(amount):
    assert amount >= 24

    if amount == 24:
        return [5, 5, 7, 7]
    if amount == 25:
        return [5, 5, 5, 5, 5]
    if amount == 26:
        return [5, 7, 7, 7]
    if amount == 27:
        return [5, 5, 5, 5, 7]
    if amount == 28:
        return [7, 7, 7, 7]
    
    coins = change_5_7(amount - 5)
    coins.append(5)
    
    return coins

def test_change():
    for i in range(24, 1001):
        try:
            print(f'amount {i} -> {change_5_7(i)}')
        except Exception as err:
            print(f'amount {i} gives -> {err.__repr__()}')

test_change()

def summation():
    sum = 0
    for n in range(1, 100):
        sum += 1/(n*(n+1))
        print(f'1/{n}*{n+1}')
    return sum
print(summation())
