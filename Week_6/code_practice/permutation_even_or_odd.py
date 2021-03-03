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

# def is_permutation_even(permutaion):
#     sign = 0 # sign = the number of transposition mod 2
#     counter = 0
#     s = 0 # first s elements are at right places
#     n = len(permutaion)

#     while s < n:
#         u = s
#         t = u
#         minmal_index = t

#         while u < n - 1:
#             u += 1
#             if permutaion[u] < permutaion[t]:
#                 t = u
#         if t != minmal_index:
#             tmp = permutaion[s]
#             permutaion[s] = permutaion[t]
#             permutaion[t] = tmp
#             sign = 1 - sign
#             counter += 1
#         s += 1
#     return permutaion, sign, counter


    
def classify_permutation(arr):
    sign = 0 # sign is the number of transposition mod 2
    counter = 0 # the number of tranposition made, at begining is 0
    s = 0 # first s elements are at the right places
    n = len(arr) # the number of elements in the array

    while s < n:
        u = s
        t = u # arr[t] is minimal among arr[s] .. a[u]
        minmal_index = t

        while u < n - 1:
            u += 1
            if arr[u] < arr[t]:
                t = u
        if t != minmal_index:
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

print('-' * 80)
print('Permutation', '|', 'Sign' , '|', '# Transpositions')
print(classify_permutation([5, 2, 3, 1]))
print(classify_permutation([8, 13, 1, 9, 2, 5, 3]))
print(classify_permutation([5, 3, 2, 1]))