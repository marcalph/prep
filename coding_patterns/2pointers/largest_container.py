def largest_container(heights: list[int] = [2, 7, 8, 3, 7, 6]) -> int:
    left, right = 0, len(heights) - 1
    running_max = 0
    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        running_max = max(area, running_max)
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
    return running_max


if __name__ == "__main__":
    print(largest_container())
