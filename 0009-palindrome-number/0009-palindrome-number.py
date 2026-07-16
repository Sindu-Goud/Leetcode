class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x 
        reversed = 0
        
        while temp  > 0 :
            digit = temp % 10 
            reversed = reversed * 10 + digit 
            temp  = temp // 10 
        if x == reversed :
            return True
        else:
            return False