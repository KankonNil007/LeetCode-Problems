class Solution(object):
    def reverse(self, x):
        str1 = str(x)
        if (str1.startswith("-")):
            str2 = str1[1:]
            chk2 = int("-" + str2[::-1])
            if (chk2 < -pow(2, 31)):
                return 0
            else:
                return chk2
        else:
            chk = int(str1[::-1])
            if (chk > (pow(2, 31) - 1)):
                return 0
            else:
                return chk