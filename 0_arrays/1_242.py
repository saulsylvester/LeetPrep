# https://leetcode.com/problems/valid-anagram/submissions/1586983455/?envType=problem-list-v2&envId=oizxjoit

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t): #If not length-wise , not correct.
            if set(s) == set(t): #If not same letters, not correct:
                if Counter(s) == Counter(t):
                    return True

        return False

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
