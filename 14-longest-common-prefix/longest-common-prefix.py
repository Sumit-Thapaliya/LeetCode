class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for s in strs:
                if i >= len(s) or s[i] != char:
                    return prefix

            prefix += char

        return prefix