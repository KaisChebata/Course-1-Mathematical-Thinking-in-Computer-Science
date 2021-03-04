"""
Even permutations

This task (solving the 15-puzzle) contains  several parts. 
To find whether a solution exists, we need to know 
whether a given permutation is even. 
We discussed this algorithm; now you have to implement it using Python.

In Python arrays are indexed from 0, 
so a permutation p of n objects is represented by a sequence p[0],...,p[n-1]

that contains numbers 0,1,2,...,n-1 (each number appears exactly once). 
In Python language,

def is_permutaion(permutaion):
    return (set(permutaion) == set(range(0, len(permutaion))))

print (is_permutation([0]))
print (is_permutation([0,2,1]))
print (is_permutation([1,2,3]))
(the first two calls give True, and the third gives False)
"""
def is_permutation(permutaion):
    return (set(permutaion) == set(range(0, len(permutaion))))

print (is_permutation([0]))
print (is_permutation([0,2,1]))
print (is_permutation([1,2,3]))
