from sqlalchemy import all_
# https://leetcode.com/problems/valid-anagram/submissions/1586983455/?envType=problem-list-v2&envId=oizxjoit
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        return Counter(s) == Counter(t)

"""
Given two strings s and t, return true if t is an

of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false



Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

"""


if __name__ == "__main__":
    solution = Solution()
    all_passed = True
    test_number = 1

    def run_test(s_input, t_input, expected_output, all_passed = all_passed, test_number = test_number):

        print(f"--- Test Case {test_number} ---")
        print(f"Input s: \"{s_input}\", t: \"{t_input}\"")
        result = solution.isAnagram(s_input, t_input)
        print(f"Expected: {expected_output}")
        print(f"Output:  {result}")
        try:
            assert result == expected_output
            print("Result: PASSED\n")
        except AssertionError:
            print(f"Result: FAILED - Input: s=\"{s_input}\", t=\"{t_input}\, Expected: {expected_output}, Got: {result}\n")
            all_passed = False
        test_number += 1

    run_test("anagram", "nagaram", True)
    run_test("rat", "car",False)
    run_test("hello", "helo", False)
