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

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordDict:
                    for rest in solve(end):
                        if rest == "":
                            result.append(word)
                        else:
                            result.append(word + " " + rest)

            memo[start] = result
            return result

        return solve(0)