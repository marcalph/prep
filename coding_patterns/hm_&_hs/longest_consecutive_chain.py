from typing import List


def longest_chain_of_consecutive_numbers(nums: List[int] = [1, 5, 3, 6, 7, 8, 10, 2]) -> int:
    # Write your code here
    mem = set(nums)
    longest_chain = 0
    for num in nums:
        if num - 1 not in mem:
            current_num = num
            current_chain = 1
            while (current_num + 1) in mem:
                current_num += 1
                current_chain += 1
            longest_chain = max(longest_chain, current_chain)
    return longest_chain


if __name__ == "__main__":
    print(longest_chain_of_consecutive_numbers())
