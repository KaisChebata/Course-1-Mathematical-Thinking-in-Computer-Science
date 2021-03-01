"""
Programming Assignment

An array a[1],...,a[n] is given, containing a permutation 
of numbers 1,....,n

output 0 if the permutaion is even 
(require an even number of transpositions) and 1 otherwise.
"""

# we will use sorting algorithm to count the exchanges

def classify_permutation(arr: list):
    sign = 0 # sign is the number of transposition mod 2
    s = 0 # first s elements are at the right places
    n = len(arr) # the number of elements in the array

    while s < n:
        u = s + 1
        t = u # arr[t] is minimal among arr[s+1] .. a[u]

        while u < n:
            u += 1
            if arr[u] < arr[t]:
                t = u
        tmp = arr[s + 1]
        arr[s + 1] = arr[t]
        arr[t] = tmp
        sign -= 1

        s += 1
    
    return arr

print(classify_permutation([5, 2, 3, 1]))