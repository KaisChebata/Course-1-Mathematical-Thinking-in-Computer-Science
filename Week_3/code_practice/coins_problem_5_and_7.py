"""
Question 1

Imagine we have only 5- and 7-coins. 
One can prove that any large enough integer amount can be paid using only such coins. 
Yet clearly we cannot pay any of numbers 1, 2, 3, 4, 6, 8, 9 with our coins. 
What is the maximum amount that cannot be paid?

Answer: 23.

explaination:
1. if we say that we have only 7-coins, then we can pay 14 by 7 + 7
    =>  (7 + 7 - 1)  = 13 can't be paid, which is below the payable amount by 1.

2. also if we say that we have only 5-coins, then we can pay 10 by 5 + 5 
    => (5 + 5 -1) = 9 can't be paid, which is below the payable amount by 1. 

3. in the same way if we say that we have only 5- and 7-coins, 
then we can pay 24 by 7 + 7 + 5 + 5 =  (7 + 5) * 2 
    => ( 7 + 5) * 2 - 1 = 23 can't be paid, 
        which is below the payable amount by 1
"""

"""
Question 2

Develop a Python method change(amount) that for any integer amount 
in the range from 24 to 1000 returns a list consisting of numbers 5 and 7 only, 
such that their sum is equal to amount. 
For example, change(28) may return [7, 7, 7, 7], 
while change(49) may return [7, 7, 7, 7, 7, 7, 7] or 
[5, 5, 5, 5, 5, 5, 5, 7, 7] or [7, 5, 5, 5, 5, 5, 5, 5, 7].

To solve this quiz, implement the method change(amount) on your machine, 
test it on several inputs, 
and then paste your code in the field below and press the submit quiz button. 
Your submission should contain the change method only 
(in particular, make sure to remove all print statements).

def change(amount):
  if amount == 24:
    return [5, 5, 7, 7]
    
  # complete this method
"""

def change(amount):
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
	
	coins = change(amount - 5)
	coins.append(5)

	return coins

def test_change():
    for amount in range(23, 1001):
        try:
            print('amount {} -> {}'.format(amount, change(amount)))
        except Exception as error:
            print('amount {} have error: {}'.format(amount, error.__repr__()))

test_change()