class Solution(object):
    def isPalindrome(self, s):
        new_s = "".join(char for char in s if char.isalnum())

        new_s = new_s.lower()
        
        if (new_s == new_s[::-1]):
            return True
        else:
            return False