def shift_zeroes_to_the_end(nums: list[int] = [0, 1, 0, 3, 2]) -> list[int]:
    insert_pos = 0  # slow/writer

    for i in range(len(nums)):  # fast/reader
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1

    return nums


# Walkthrough: [0, 1, 0, 3, 2]
#
#   i  insert_pos  action          result
#   ─────────────────────────────────────────
#   0      0       skip (zero)     [0, 1, 0, 3, 2]
#   1      0       swap → 1        [1, 0, 0, 3, 2]
#   2      1       skip (zero)     [1, 0, 0, 3, 2]
#   3      1       swap → 2        [1, 3, 0, 0, 2]
#   4      2       swap → 3        [1, 3, 2, 0, 0]
#                                   ───────┬─────
#                                   non-zero│zeros


if __name__ == "__main__":
    print(shift_zeroes_to_the_end())
