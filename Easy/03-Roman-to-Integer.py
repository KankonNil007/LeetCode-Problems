class Solution(object):
    def romanToInt(self, s):
        Num = 0
        for i in range(len(s)):
            if (s[i] == 'M'):
                if (s[i - 1] == 'C' and (i-1) >= 0):
                    Num -= 100
                    Num += 900
                else:
                    Num += 1000
            elif (s[i] == 'D'):
                if (s[i - 1] == 'C' and (i-1) >= 0):
                    Num -= 100
                    Num += 400
                else:
                    Num += 500
            elif (s[i] == 'C'):
                if (s[i - 1] == 'X' and (i-1) >= 0):
                    Num -= 10
                    Num += 90
                else:
                    Num += 100
            elif (s[i] == 'L'):
                if (s[i - 1] == 'X' and (i-1) >= 0):
                    Num -= 10
                    Num += 40
                else:
                    Num += 50
            elif (s[i] == 'X'):
                if (s[i - 1] == 'I' and (i-1) >= 0):
                    Num -= 1
                    Num += 9
                else:
                    Num += 10
            elif (s[i] == 'V'):
                if (s[i - 1] == 'I' and (i-1) >= 0):
                    Num -= 1
                    Num += 4
                else:
                    Num += 5
            elif (s[i] == 'I'):
                Num += 1

        return Num