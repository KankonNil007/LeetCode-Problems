class Solution(object):
    def isValid(self, s):
        stack = []
        brackets = { "(": ")", "{": "}", "[": "]"}

        for i in s:
            if i in brackets.keys():
                stack.append(brackets[i])
            elif i in brackets.values():
                if (not stack):
                    return False
                elif (i == stack[-1]):
                    stack.pop()
                else:
                    return False
        
        if (not stack):
            return True
        else:
            return False