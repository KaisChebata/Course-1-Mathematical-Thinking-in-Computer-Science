def iterative_factorial(num):
	assert num > 0
	result = 1

	for i in range(1, num + 1):
		result *= i
	return result

def recursive_factorial(num):
	assert num > 0

	if num == 1:
		return 1
	else:
		return num * recursive_factorial(num - 1)

print('iterative factorial ......')
print('iterative_factorial(5) ->', iterative_factorial(5))
print('-------------------------------------------------')
print('recursive factorial ......')
print('recursive_factorial(5) ->', recursive_factorial(5))