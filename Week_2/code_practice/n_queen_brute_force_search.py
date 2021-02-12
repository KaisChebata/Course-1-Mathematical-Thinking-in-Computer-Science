import itertools as it

def is_solution(perm):
	for (col1, col2) in it.combinations(range(len(perm)), 2):
		if abs(col1 - col2) == abs(perm[col1] - perm[col2]):
			return False
	return True

assert is_solution([1, 3, 0, 2]) == True
assert is_solution([3, 1, 0, 2]) == False

print('is_solution([1, 3, 0, 2]):', is_solution([1, 3, 0, 2]))

print('is_solution([2, 0, 3, 1]):', is_solution([2, 0, 3, 1]))
print('is_solution([3, 1, 0, 2]):', is_solution([3, 1, 0, 2]))

print('is_solution([1, 2, 0, 3]):', is_solution([1, 2, 0, 3]))
print('is_solution([0, 4, 7, 5, 2, 6, 1, 3]):', is_solution([0, 4, 7, 5, 2, 6, 1, 3]))

print()	

def all_solutions_brute_force(length):

	all_possible_permuntations = it.permutations(range(length))
	solution_counter = 0

	for perm in all_possible_permuntations:
		if is_solution(perm):
			print(perm)
			solution_counter += 1

	return solution_counter

length = 8

print('all possible solutions number for', length,\
	'queen problem =', all_solutions_brute_force(length), 'solutions'
	)