class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""

        for j in range(len(min(strs, key=len))):
            count = 0
            for i in strs:
                if (not i[j].startswith(strs[0][j])):
                    count = 0
                    break
                count = 1
            if (count == 0):
                break
            elif(count == 1):
                prefix += i[j]

        return prefix