class Solution:
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        memo = {}

        def solve(start):
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            result = []

            for word in wordDict:
                if s.startswith(word, start):
                    for rest in solve(start + len(word)):
                        if rest == "":
                            result.append(word)
                        else:
                            result.append(word + " " + rest)

            memo[start] = result
            return result

        return solve(0)