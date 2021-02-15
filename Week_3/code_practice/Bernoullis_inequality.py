# import matplotlib.pyplot as plt
# import numpy as np

# # You can play with the range of values for n and with the base 1.02, see what changes
# sample = 200
# x = np.arange(sample)
# # This is used to plot the graph of 1.02^n, it is blue on the picture below
# y = 1.02 ** x
# plt.plot(x, y)
# plt.xlabel('n')
# plt.ylabel('Money($)')
# # This is used to plot the graph of 1 + 0.02 * n, it is green on the picture below
# z = 1 + 0.02 * x
# plt.plot(x, z)
# plt.show()

# Computes how much money you will have on day *day*, if you start with *starting_amount* of cash
# and earn *earn_percent* percents of what you already have every day.
def how_much_money(starting_amount, earn_percent, days_num):
    added_percent = 1 + (earn_percent / 100.0)
    return starting_amount * (added_percent ** (days_num - 1))

def how_much_printer(starting_amount, earn_percent, days_num):
    print(f'If you start with ${starting_amount} and earn {earn_percent}% each day, '
          f'you will have more than ${how_much_money(starting_amount, earn_percent, days_num):.0f} '
          f'on day {days_num}!')

# Prints what will happen by day 350 if you start with $1000 and earn 2% every day
# Feel free to play with the parameters
how_much_printer(1000, 2, 350)

# Compute the number of the first day when your wealth will exceed *target_amount*,
# if you start with *starting_amount* of cash and earn *earn_percent* percents every day
def goal_day(starting_amount, earn_percent, target_amount):
    added_percent = 1 + (earn_percent / 100.0)
    amount = starting_amount
    day = 1

    while amount < target_amount:
        day += 1
        amount *= added_percent
    
    return day

def first_day_printer(starting_amount, earn_percent, target_amount):
    print(f'If you start with ${starting_amount} and earn {earn_percent}% each day, '
          f'you will have more than ${target_amount} on day '
          f'{goal_day(starting_amount, earn_percent, target_amount)} for the first time!')

# Prints when you will get more than $1000000 for the first time, if you start with $1000
# and earn 2% every day.
first_day_printer(1000, 2, 1000000)

