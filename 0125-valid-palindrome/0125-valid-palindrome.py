class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ""
        for ch in s :
            if ch.isalnum():
                reverse += ch.lower() 
        return  reverse == reverse[::-1]
        
