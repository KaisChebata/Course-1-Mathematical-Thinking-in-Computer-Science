
def can_be_extended_to_solution(perm):
	"""can_be_extended_to_solution(lst) -> bool

	return True if the argument (perm) is a correct solution, 
	where we check if the last added queen doesn't attack any other 
	previous queen in the perm (board).

	>>> can_be_extended_to_solution([1, 3, 0, 2])
	True
	>>> can_be_extended_to_solution([3, 1, 0, 2])
	False
	"""
	i = len(perm) - 1 #take the index of last added queen
	for j in range(i):
		if abs(i - j) == abs(perm[i] - perm[j]): #test if the last queen doesn't attack others.
			return False
	return True

def generate_permutations(perm, n):
	"""(lst, int) -> None

	generate all possible permutations of length (n) starting from (perm), 
	we can start from empty perm or with some element in it, 
	and then print them all (perms).

	>>> generate_permutations([], 3)
	[0, 1, 2]
	[0, 2, 1]
	[1, 0, 2]
	[1, 2, 0]
	[2, 0, 1]
	[2, 1, 0]
	"""
	if len(perm) == n:
		print(perm)
		return
	
	for k in range(n):
		if k not in perm:
			perm.append(k)
			generate_permutations(perm, n)
			perm.pop()

def extend_backtracking_solution(perm, board_size):
	if len(perm) == board_size:
		print(perm)
		exit()
	
	for k in range(board_size):
		if k not in perm:
			perm.append(k)
			if can_be_extended_to_solution(perm):
				extend_backtracking_solution(perm, board_size)
			perm.pop()

print("testing generate_permutations([], 3): ")
generate_permutations([], 3)
print()
print("testing if we can extend [3, 1, 0] or not :", 
	can_be_extended_to_solution([3, 1, 0]))

# print("testing extend_backtracking_solution([], 4): ")
# extend_backtracking_solution(perm = [], board_size = 4)

print("testing extend_backtracking_solution([], 20) : ")
extend_backtracking_solution(perm=[], board_size= 20)
