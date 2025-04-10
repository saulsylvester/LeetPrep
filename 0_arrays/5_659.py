class Solution:
    def encode(self, strs: list[str]) -> str:
        # return ";:".join(strs)
        # Count the number of characters in each string
        # the result will be a string with the number of characters first, then "##", then the string itself
        res = []
        for i in strs:
            res.append(str(len(i)) + "##"+i)

        return "".join(res)


    def decode(self, s: str) -> list[str]:
        # Example: '4##lint4##code4##love3##you'

        # Iterate through string
        # If we find a number, we know that the next two characters will be "##"
        # After ## we need "n" positions, and then append to res

        res = []
        for char in s:
            if char.isdigit():
                n = int(char)
                res.append(s[s.index("##")+2:s.index("##")+2+n])
                s = s[s.index("##")+2+n:]
        return res

        # return s.split(";:")



"""
659 · Encode and Decode Strings

Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Because the string may contain any of the 256 legal ASCII characters, your algorithm must be able to handle any character that may appear

Do not rely on any libraries, the purpose of this problem is to implement the "encode" and "decode" algorithms on your own


Example1

Input: ["lint","code","love","you"]

Output: ["lint","code","love","you"]

Explanation:

One possible encode method is: "lint:;code:;love:;you"

Example2

Input: ["we", "say", ":", "yes"]

Output: ["we", "say", ":", "yes"]

Explanation:

One possible encode method is: "we:;say:;:::;yes"
"""

import unittest
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        strs = ["lint", "code", "love", "you"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)

    def test_example_2(self):
        strs = ["we", "say", ":", "yes"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)

    def test_empty_list(self):
        strs = []
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)

    def test_single_empty_string(self):
        strs = [""]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)

    def test_multiple_empty_strings(self):
        strs = ["", "", ""]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)

    def test_strings_with_special_characters(self):
        strs = ["hello, world!", "@#$%", "123\n456", "\t\r"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)

    def test_strings_with_long_characters(self):
        strs = ["a" * 200, "b" * 150]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)

    def test_strings_with_numbers(self):
        strs = ["1", "12", "123"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)

    def test_strings_with_null_characters(self):
        strs = ["hello\x00world", "\x00"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)

if __name__ == '__main__':
    unittest.main()
