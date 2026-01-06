from typing import List

    
from typing import List
from collections import defaultdict

def geometric_sequence_triplets(nums: List[int], r: int) -> int:
    potential_pairs = defaultdict(int)
    potential_triplets = defaultdict(int)
    # Total number of valid triplets found
    count = 0

    for n in nums:
        # If n completes any triplet, add the number of such triplets to count
        count += potential_triplets[n]

        # If n can be the second element of any triplet, 
        # then n*r can be the third element in those triplets
        if n in potential_pairs:
            potential_triplets[n * r] += potential_pairs[n]

        # Every number can start a new triplet, so n*r can be its potential second element
        potential_pairs[n * r] += 1

    return count

