# https://leetcode.com/problems/group-anagrams/description/?envType=problem-list-v2&envId=oizxjoit
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hmap = {}
        for s in strs:
            s_list = list(s)
            s_list.sort()
            s_order = "".join(s_list)
            if s_order not in hmap.keys():
                s_order = "".join(s_list)
                hmap[s_order] = [s]
            else:
                hmap[s_order] = hmap[s_order] + [s]
        return list(hmap.values())


"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

"""

def canonical_form(list_of_lists):
    # 1. Sort each inner list (group of anagrams) alphabetically
    sorted_inner_lists = [sorted(inner_list) for inner_list in list_of_lists]

    # 2. Sort the outer list of sorted inner lists.
    # We use 'str(x)' as a key to ensure consistent sorting of lists themselves,
    # as Python's default list comparison can be element-by-element.
    return sorted(sorted_inner_lists, key=lambda x: str(x))


import unittest
class TestGroupAnagrams(unittest.TestCase):

    def setUp(self):
        # This method runs before each test_ method
        self.solution = Solution()

    # Custom assertion method for anagram groups
    def _assert_anagram_groups_equal(self, actual, expected, message=""):
        # Convert both actual and expected to canonical form before asserting equality
        self.assertEqual(canonical_form(actual), canonical_form(expected), message)

    def test_example_1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        expected = [["bat"], ["nat","tan"], ["ate","eat","tea"]]
        result = self.solution.groupAnagrams(strs)
        self._assert_anagram_groups_equal(result, expected, f"Test Case 1 Failed: Input={strs}")

    def test_example_2_empty_string(self):
        strs = [""]
        expected = [[""]]
        result = self.solution.groupAnagrams(strs)
        self._assert_anagram_groups_equal(result, expected, f"Test Case 2 Failed: Input={strs}")

    def test_example_3_single_char(self):
        strs = ["a"]
        expected = [["a"]]
        result = self.solution.groupAnagrams(strs)
        self._assert_anagram_groups_equal(result, expected, f"Test Case 3 Failed: Input={strs}")

    def test_no_anagrams(self):
        strs = ["abc", "def", "ghi"]
        expected = [["abc"], ["def"], ["ghi"]]
        result = self.solution.groupAnagrams(strs)
        self._assert_anagram_groups_equal(result, expected, f"Test Case No Anagrams Failed: Input={strs}")

    def test_all_anagrams(self):
        strs = ["abc", "bca", "cab"]
        expected = [["abc", "bca", "cab"]]
        result = self.solution.groupAnagrams(strs)
        self._assert_anagram_groups_equal(result, expected, f"Test Case All Anagrams Failed: Input={strs}")

    def test_mixed_groups(self):
        strs = ["listen", "silent", "enlist", "hello", "world", "olleh"]
        expected = [
            ["listen", "silent", "enlist"],
            ["hello", "olleh"],
            ["world"]
        ]
        result = self.solution.groupAnagrams(strs)
        self._assert_anagram_groups_equal(result, expected, f"Test Case Mixed Groups Failed: Input={strs}")

    def test_longer_strings(self):
        strs = ["topcoder", "redocpot", "programming", "gmrpromgina"]
        expected = [
            ["topcoder", "redocpot"],
            ["programming", "gmrpromgina"]
        ]
        result = self.solution.groupAnagrams(strs)
        self._assert_anagram_groups_equal(result, expected, f"Test Case Longer Strings Failed: Input={strs}")

    def test_duplicates_in_input(self):
        strs = ["a", "a", "b", "a"]
        expected = [["a", "a", "a"], ["b"]]
        result = self.solution.groupAnagrams(strs)
        self._assert_anagram_groups_equal(result, expected, f"Test Case Duplicates in Input Failed: Input={strs}")

if __name__ == '__main__':
    unittest.main()
