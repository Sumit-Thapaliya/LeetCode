class Solution(object):
    def isMatch(self, s, p):
        memo = {}

        def match(i, j):
            # Both strings finished
            if i == len(s) and j == len(p):
                return True

            # Pattern finished but string is not
            if j == len(p):
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            # Does current character match?
            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )

            # If next character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':

                # Choice 1: use zero of this character
                skip = match(i, j + 2)

                # Choice 2: use one character, if current matches
                use = first_match and match(i + 1, j)

                result = skip or use

            else:
                # Normal character
                result = first_match and match(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return match(0, 0)