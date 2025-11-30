def josephus(n, k):  # O(n^2)
    # Complete solve function
    people = list(range(n))  # Create a list of people numbered 1 to n
    index = 0  # Start from the first person

    while len(people) > 1:
        index = (index + k - 1) % len(people)  # Calculate the next index to remove
        people.pop(index)  # Remove the person at the index

    return people[0]  # Return the last remaining person


import sys

sys.setrecursionlimit(2000)


# (old_num - k) % n   = new_num
# (jos(n, k) - k) % n = jos(n-1, k)
def josephus_recursive(n, k):
    # Base case: the survivor is at position 0 (0-indexed)
    if n == 1:
        return 0
    else:
        return (josephus_recursive(n - 1, k) + k) % n


# binary jos problem (k=2)
####
# n even
# old_num = 2* new_num
# jos(n, 2) = 2 * jos(n/2, 2)   >> after the first traversal n/2 remain
####
# n odd
# old_num  =  2* new_num -2
# jos(n,2) = 2*jos((n+1)/2, 2) -2


# even faster with powers of 2 for the binary jos porblem
# n = 2ˆt+l
# after first traversal l are killed, meaning jos(n, 2)= jos(2ˆt+l, 2) = 2l
def bin_jos(n):
    return (n ^ (1 << (int.bit_length(n) - 1 - 1))) << 1
