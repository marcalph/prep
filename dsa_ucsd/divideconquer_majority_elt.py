from collections import Counter


def majority_element_naive(elements):
    cnt = Counter(elements)
    return int(cnt.most_common(1)[0][1] > len(elements) / 2)


def majority_element(elements, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return elements[left]
    middle = (left + right) // 2
    x = majority_element(elements, left, middle)
    if elements[left:right].count(x) > (right - left) / 2:
        return x
    x = majority_element(elements, middle, right)
    if elements[left:right].count(x) > (right - left) / 2:
        return x
    return -1


# If a majority exists in the original list, at least one duplicate pair must exist if the list is partioned into pairs. If a duplicate pair of an element does not exist, then  that element can not have more than n/2 copies in the list.
# After running through the list and discarding any elements not in a duplicate pair, we can take the remaining elements and count their instances in the original list to see if any have >n/2.
# example:
# [A, B, B, B, A, C, C, C, B]
# AB BB AC CC CB
# B, C
# count instances of B and C in original list


if __name__ == "__main__":
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
