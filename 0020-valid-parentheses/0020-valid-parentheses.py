class Solution:
    def isValid(self, s):
        stack = []
        pairs = {"(" : ")" , "{": "}", "[": "]"}
        for brackets in s:
            if brackets in pairs:
                stack.append(brackets)
            elif len(stack) == 0 or brackets != pairs[stack.pop()]:
                return False 
        return len(stack) == 0 

        