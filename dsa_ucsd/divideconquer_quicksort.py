from random import randint


def partition(array, left, right):
    # write your code here
    pivot = array[left]
    m1 = left
    for i in range(left+1, right+1):
        if array[i]<=pivot:
            m1+=1
            array[i], array[m1] = array[m1], array[i]
    array[left], array[m1] = array[m1], array[left]
    return m1
    

def quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1= partition(array, left, right)
    quick_sort(array, left, m1 - 1)
    quick_sort(array, m1 + 1, right)

def partition3(arr, l, r):
    pivot = arr[l]  # Choose the leftmost element as the pivot
    lt = l  # Pointer for elements < pivot
    gt = r  # Pointer for elements > pivot
    i = l  # Current index

    while i <= gt:
        if arr[i] < pivot:  
            arr[lt], arr[i] = arr[i], arr[lt]  # Swap and expand the left region
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]  # Swap and shrink the right region
            gt -= 1
        else:
            i += 1  # Element equals pivot, move forward

    return lt, gt  # Return the boundaries of the pivot section


def all_in_one_quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[randint(0, len(lst) - 1)]

    smaller = [x for x in lst if x < pivot]
    equal = [x for x in lst if x == pivot]
    larger = [x for x in lst if x > pivot]

    smaller = quick_sort(smaller)
    larger = quick_sort(larger)

    return smaller + equal + larger


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)