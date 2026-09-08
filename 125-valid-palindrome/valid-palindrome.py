class Solution(object):
    def isPalindrome(self, s):
        a="".join(num.lower()for num in s if num.isalnum())
        if a== a[::-1]:
            return True
        else:
            return False
    
        