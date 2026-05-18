class Solution(object):
    def lengthOfLastWord(self, s):
        len = 0
        revS = s[::-1]
        revS = revS.lstrip()

        for i in revS:
            if i == " ":
                break
            else:
                len += 1
        return len
            