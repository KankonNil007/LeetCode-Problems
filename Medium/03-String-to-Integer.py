class Solution(object):
    def myAtoi(self, s):
        strpS = s.strip()
        newStr = ""

        for i, word in enumerate(strpS):
            if (word in ["-", "+"] and i == 0):
                newStr += word
                continue
            if (word.isnumeric()):
                newStr += word
            if ((not word.isnumeric())):
                break

        if (not newStr or newStr == "+" or newStr == "-"):
            newStr = "0"

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if int(newStr) > INT_MAX:
            return INT_MAX
        if int(newStr) < INT_MIN:
            return INT_MIN
        return int(newStr)