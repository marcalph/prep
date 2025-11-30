from itertools import combinations


def merge_and_count(b, c):
    """Merge two sorted arrays b and c while counting inversions."""
    a = []
    i = j = inv_count = 0  # Pointers for b, c & inversion counter

    while i < len(b) and j < len(c):
        if b[i] <= c[j]:
            a.append(b[i])  # Take from b (no inversion)
            i += 1
        else:
            a.append(c[j])  # Take from c (inversions found)
            inv_count += len(b) - i  # All remaining b[i:] are greater
            j += 1

    # Append remaining elements
    a.extend(b[i:])
    a.extend(c[j:])

    return a, inv_count  # Return merged list and count


def count_inversions(arr):
    """Returns sorted array and number of inversions in O(n log n)."""
    if len(arr) <= 1:
        return arr, 0  # Base case: no inversions

    mid = len(arr) // 2
    left_sorted, left_inv = count_inversions(arr[:mid])  # Left half
    right_sorted, right_inv = count_inversions(arr[mid:])  # Right half
    merged_sorted, split_inv = merge_and_count(
        left_sorted, right_sorted
    )  # Merge & count cross-inversions

    total_inv = left_inv + right_inv + split_inv  # Total inversions
    return merged_sorted, total_inv


if __name__ == "__main__":
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(count_inversions(elements)[1])
