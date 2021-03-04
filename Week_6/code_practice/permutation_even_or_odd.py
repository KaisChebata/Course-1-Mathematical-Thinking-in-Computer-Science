"""
Programming Assignment

An array a[1],...,a[n] is given, containing a permutation 
of numbers 1,....,n

output 0 if the permutaion is even 
(require an even number of transpositions) and 1 otherwise.
"""

# we will use sorting algorithm to count the exchanges

# Psedou code for sorting and find if permutation is even or odd
'''
// sorting a[1]..a[n]
sign=0 // sign = the number of transpositions mod 2
s=0 // first s elements are at the right places
while (s<n){
    u=s+1; t=u; //a[t] is minimal among a[s+1]..a[u];
    while (u<n){
        u=u+1;
        if a[u]<a[t] {t=u;}
    }
    // a[t] is minimal among a[s+1]..a[n]
    tmp=a[s+1]; a[s+1]=a[t]; a[t]=tmp; sign=1-sign;

    Hints: (a) will the loop terminate? 
           (b) what happens with the identity permutation 
           (already sorted array)?
}
'''

def classify_permutation(arr):
    sign = 0 # sign is the number of transposition mod 2
    counter = 0 # the number of tranposition made, at begining is 0
    s = 0 # first s elements are at the right places
    n = len(arr) # the number of elements in the array

    while s < n:
        u = s
        t = u # arr[t] is minimal among arr[s] .. a[u]
        minimal_index = t

        while u < n - 1:
            u += 1
            if arr[u] < arr[t]:
                t = u
        if t != minimal_index:
            tmp = arr[s]
            arr[s] = arr[t]
            arr[t] = tmp
            sign = 1 - sign
            counter += 1
        s += 1

    return arr, sign, counter

# Examples:
# I:
# 5 2 3 1
# 1 2 3 5: 1
# ----------
# Transposition = 1

# II: 
# 8 13 1 9 2 5 3
# 1 13 8 9 2 5 3: 1
# 1 2 8 9 13 5 3: 2
# 1 2 3 9 13 5 8: 3
# 1 2 3 5 13 9 8: 4
# 1 2 3 5 8 9 13: 5
# ------------------
# Transpositions = 5

# III:
# 5 3 2 1
# 1 3 2 5: 1
# 1 2 3 5: 2
# ------------------
# Transpositions = 2

# IV:
# 4 2 1 8 5 3 6 7
# 1 2 4 8 5 3 6 7: 1
# 1 2 3 8 5 4 6 7: 2
# 1 2 3 4 5 8 6 7: 3
# 1 2 3 4 5 6 8 7: 4
# 1 2 3 4 5 6 7 8: 5
# ------------------
# Transpositions = 5

print('-' * 80)
print('Permutation', '|', 'Sign' , '|', '# Transpositions')
print(classify_permutation([5, 2, 3, 1]))
print(classify_permutation([8, 13, 1, 9, 2, 5, 3]))
print(classify_permutation([5, 3, 2, 1]))
print(classify_permutation([4, 2, 1, 8, 5, 3, 6, 7]))
print(classify_permutation([4, 3 ,2, 1]))
print(classify_permutation([0,3,2,4,5,6,7,1,9,8]))