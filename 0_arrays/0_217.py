# https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=oizxjoit
from curses.ascii import SUB
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        pass

"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true



Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109


"""


if __name__ == "__main__":
    solution = Solution()
    all_passed = True
    test_number = 1

    # Test Case 1
    nums1 = [1, 2, 3, 1]
    expected1 = True
    result1 = solution.containsDuplicate(nums1)
    try:
        assert result1 == expected1

    except AssertionError as e:
        print(f"Test Case {test_number}: Input={nums1}, Expected={expected1}, Output={result1}")
        print(e)
        all_passed = False
    test_number += 1

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    expected2 = False
    result2 = solution.containsDuplicate(nums2)
    try:
        assert result2 == expected2

    except AssertionError as e:
        print(f"Test Case {test_number}: Input={nums2}, Expected={expected2}, Output={result2}")
        print(e)
        all_passed = False
    test_number += 1

    # Test Case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    expected3 = True
    result3 = solution.containsDuplicate(nums3)
    try:
        assert result3 == expected3
    except AssertionError as e:
        print(f"Test Case {test_number}: Input={nums3}, Expected={expected3}, Output={result3}")
        print(e)
        all_passed = False
    test_number += 1

    # Add more test cases
    nums4 = []
    expected4 = False
    result4 = solution.containsDuplicate(nums4)
    try:
        assert result4 == expected4
    except AssertionError as e:
        print(f"Test Case {test_number}: Input={nums4}, Expected={expected4}, Output={result4}")
        print(e)
        all_passed = False
    test_number += 1

    nums5 = [5]
    expected5 = False
    result5 = solution.containsDuplicate(nums5)
    try:
        assert result5 == expected5
    except AssertionError as e:
        print(f"Test Case {test_number}: Input={nums5}, Expected={expected5}, Output={result5}")
        print(e)
        all_passed = False
    test_number += 1

    nums6 = [-1, -1]
    expected6 = True
    result6 = solution.containsDuplicate(nums6)
    try:
        assert result6 == expected6
    except AssertionError as e:
        print(f"Test Case {test_number}: Input={nums6}, Expected={expected6}, Output={result6}")
        print(e)
        all_passed = False
    test_number += 1

    if all_passed:
        print("\nAll passed!")
        import sys
        import os
        import re
        import subprocess
