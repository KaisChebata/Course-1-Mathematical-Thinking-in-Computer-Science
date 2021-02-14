"""
Number of Moves to Solve the Hanoi Towers Puzzle
1. Question 1

The number of moves required to solve the Hanoi Towers puzzle for 
n = 1 and n = 2 discs is equal to 1 and 3, respectively. 
Implement the recursive solution for the Hanoi Towers 
(described in the lectures) and count the number of moves for n = 6 discs.
"""

moves_num = 0
def hanoi_tower_moves(disks_num, source, helper, target):
	global moves_num
	
	if disks_num == 1:
		print('Move disk 1 from {} to {}.'.format(source, target))
		moves_num += 1 # 1
		return
	hanoi_tower_moves(disks_num - 1, source, target, helper)
	print('Move disk {} from {} to {}.'.format(disks_num, source, target))
	moves_num += 1 # 2
	hanoi_tower_moves(disks_num - 1, helper, source, target)

def moves_number(disk_num):
	if disk_num == 1:
		return 1
	return moves_number(disk_num - 1) * 2 + 1 

hanoi_tower_moves(6, 'source', 'intermediate', 'target')
print(moves_num)
print('-------------------------------------')


print('number of moves in tower of 6 disks =', moves_number(6))
print(64*2)