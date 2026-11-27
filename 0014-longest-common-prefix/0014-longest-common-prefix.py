class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s1, s2 = min(strs), max(strs)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1