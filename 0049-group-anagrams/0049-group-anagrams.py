class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for s in strs:
            d.setdefault(tuple(sorted(s)), []).append(s)
        return list(d.values())