# https://leetcode.com/problems/two-sum/?envType=problem-list-v2&envId=oizxjoit
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


"""

import unittest
class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertCountEqual(result, expected, f"Test Case 1 Failed: Input={nums}, Target={target}, Expected={expected}, Got={result}")

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        result = self.solution.twoSum(nums, target)
        self.assertCountEqual(result, expected, f"Test Case 2 Failed: Input={nums}, Target={target}, Expected={expected}, Got={result}")

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertCountEqual(result, expected, f"Test Case 3 Failed: Input={nums}, Target={target}, Expected={expected}, Got={result}")

    # def test_negative_numbers(self):
    #     nums = [-1, -3, 5, 8]
    #     target = 2
    #     expected = [0, 3]
    #     result = self.solution.twoSum(nums, target)
    #     self.assertCountEqual(result, expected, f"Test Case Negative Numbers Failed: Input={nums}, Target={target}, Expected={expected}, Got={result}")

    def test_target_zero(self):
        nums = [10, -5, 5]
        target = 0
        expected = [1, 2]
        result = self.solution.twoSum(nums, target)
        self.assertCountEqual(result, expected, f"Test Case Target Zero Failed: Input={nums}, Target={target}, Expected={expected}, Got={result}")

    def test_duplicate_numbers_different_indices(self):
        nums = [1, 2, 2, 3]
        target = 4
        expected = [1, 2] # or [2, 1]
        result = self.solution.twoSum(nums, target)
        self.assertCountEqual(result, expected, f"Test Case Duplicate Numbers Failed: Input={nums}, Target={target}, Expected={expected}, Got={result}")

    def test_single_element_no_solution(self):
        nums = [5]
        target = 10
        # While the problem states "exactly one solution", it's good to consider
        # cases where no solution might exist in your test setup.
        # However, for this problem, we're guaranteed a solution.
        pass # No test for no solution needed as per problem statement

    def test_large_numbers(self):
        nums = [1000000000, 2000000000]
        target = 3000000000
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertCountEqual(result, expected, f"Test Case Large Numbers Failed: Input={nums}, Target={target}, Expected={expected}, Got={result}")

if __name__ == '__main__':
    unittest.main()
