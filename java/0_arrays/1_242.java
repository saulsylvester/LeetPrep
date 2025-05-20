import java.util.Arrays;

class Solution {

    public boolean isAnagram(String s, String t) {
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();

        Arrays.sort(sChars);
        Arrays.sort(tChars);

        return Arrays.equals(sChars, tChars);
    }

    // Testing
    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean allTestsPassed = true;
        int testCaseNumber = 1;

        // Test 1
        String s1 = "anagram";
        String t1 = "nagaram";
        boolean exp1 = true;
        boolean result1 = solution.isAnagram(s1, t1);
        System.out.println("--- Test Case " + testCaseNumber++ + " ---");
        System.out.println("Input s: \"" + s1 + "\", t: \"" + t1 + "\"");
        System.out.println("Expected: " + exp1);
        System.out.println("Output:   " + result1);
        if (result1 == exp1) {
            System.out.println("Result: PASSED\n");
        } else {
            System.out.println("Result: FAILED\n");
            allTestsPassed = false;
        }

        // --- Test Case 2: Not Anagrams (different characters) ---
        String s2 = "rat";
        String t2 = "car";
        boolean expected2 = false;
        boolean result2 = solution.isAnagram(s2, t2);
        System.out.println("--- Test Case " + testCaseNumber++ + " ---");
        System.out.println("Input s: \"" + s2 + "\", t: \"" + t2 + "\"");
        System.out.println("Expected: " + expected2);
        System.out.println("Output:   " + result2);
        if (result2 == expected2) {
            System.out.println("Result: PASSED\n");
        } else {
            System.out.println("Result: FAILED\n");
            allTestsPassed = false;
        }

        // --- Test Case 3: Different Lengths (should return false quickly) ---
        String s3 = "hello";
        String t3 = "helo";
        boolean expected3 = false;
        boolean result3 = solution.isAnagram(s3, t3);
        System.out.println("--- Test Case " + testCaseNumber++ + " ---");
        System.out.println("Input s: \"" + s3 + "\", t: \"" + t3 + "\"");
        System.out.println("Expected: " + expected3);
        System.out.println("Output:   " + result3);
        if (result3 == expected3) {
            System.out.println("Result: PASSED\n");
        } else {
            System.out.println("Result: FAILED\n");
            allTestsPassed = false;
        }
    }
}
