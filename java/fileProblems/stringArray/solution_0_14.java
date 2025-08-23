class solution_0_14 {

    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++) while (
            strs[i].indexOf(prefix) != 0
        ) {
            prefix = prefix.substring(0, prefix.length() - 1);
            if (prefix.isEmpty()) return "";
        }
        return prefix;
    }

    // Testing
    public static boolean check(String[] strs, String expected) {
        solution_0_14 solution = new solution_0_14();
        String result = solution.longestCommonPrefix(strs);
        return (
            (expected == null && result == null) ||
            (expected != null && expected.equals(result))
        );
    }

    public static void main(String[] args) {
        boolean[] results = {
            check(new String[] { "flower", "flow", "flight" }, "fl"),
            check(new String[] { "dog", "racecar", "car" }, ""),
            check(new String[] {}, ""),
            check(null, ""),
            check(new String[] { "alone" }, "alone"),
            check(new String[] { "test", "test", "test" }, "test"),
            check(new String[] { "abc", "ab", "" }, ""),
        };

        boolean allPassed = true;
        StringBuilder summary = new StringBuilder();
        for (boolean passed : results) {
            if (passed) summary.append(".");
            else {
                summary.append("F");
                allPassed = false;
            }
        }

        if (!allPassed) {
            System.out.println("Failed tests: " + summary.toString());
        } else {
            System.out.println(summary.toString() + "\nAll tests passed!");
        }
    }
}
