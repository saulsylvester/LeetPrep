import java.util.HashSet;

class Solution {

    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (!seen.add(num)) {
                return true;
            }
        }
        return false;
    }

    // Testing
    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean allTestsPassed = true;
        int testCaseNumber = 1;

        // Test Case 1
        int[] nums1 = { 1, 2, 3, 1 };
        boolean expected1 = true;
        boolean result1 = solution.containsDuplicate(nums1);
        System.out.println("--- Test Case " + testCaseNumber++ + " ---");
        System.out.println("Input: " + java.util.Arrays.toString(nums1)); // Print array content
        System.out.println("Expected: " + expected1);
        System.out.println("Output: " + result1);
        if (result1 == expected1) {
            System.out.println("Result: PASSED\n");
        } else {
            System.out.println("Result: FAILED\n");
            allTestsPassed = false;
        }

        // Test Case 2
        int[] nums2 = { 1, 2, 3, 4 };
        boolean expected2 = false;
        boolean result2 = solution.containsDuplicate(nums2);
        System.out.println("--- Test Case " + testCaseNumber++ + " ---");
        System.out.println("Input: " + java.util.Arrays.toString(nums2));
        System.out.println("Expected: " + expected2);
        System.out.println("Output: " + result2);
        if (result2 == expected2) {
            System.out.println("Result: PASSED\n");
        } else {
            System.out.println("Result: FAILED\n");
            allTestsPassed = false;
        }
    }
}
