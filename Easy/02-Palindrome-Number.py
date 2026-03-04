class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        newX = x[::-1]
        if (x == newX):
            return True
        else:
            return False