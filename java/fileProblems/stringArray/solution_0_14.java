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

    // tests
    public static void main(String[] args) {
        solution_0_14 solution = new solution_0_14();
        System.out.println(
            solution.longestCommonPrefix(
                new String[] { "flower", "flow", "flight" }
            )
        );
        System.out.println(
            solution.longestCommonPrefix(
                new String[] { "dog", "racecar", "car" }
            )
        ); // ""
        System.out.println(solution.longestCommonPrefix(new String[] {})); // ""
        System.out.println(solution.longestCommonPrefix(null));
    }
}
