"""
prove that monetaty amount starting from 8 can be 
paid using coins of denominations 3 and 5.
"""

"""
speculating:

1- we know that we can definitely pay 8.
2- but we can also pay 11 = 8 + 3 (add one 3 coin).
3- then 14, 17, 20, etc ....
4- similary 9 gives 12, 15, 18, 21, etc ...
5- while 10 gives us 13, 16, 19, 22, etc ...
"""

# from speculating above we can implement a recursive procedure

def change(amount):
	assert amount >= 8

	if amount == 8:
		return [3, 5]
	if amount == 9:
		return [3 ,3, 3]
	if amount == 10:
		return [5, 5]

	coins = change(amount - 3)
	coins.append(3)

	return coins

print(change(31))


