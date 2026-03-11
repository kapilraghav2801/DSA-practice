class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s1 = "".join(s.split())
        s1 = "".join(c.lower() for c in s if c.isalnum()) 

        if s1 == s1[::-1]:
            return True

        else:
            return False



#2 pointer approach
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s1 = "".join(s.split())
        s1 = "".join(c.lower() for c in s if c.isalnum()) 

        left, right = 0, len(s1) - 1 
        while left < right:
            if s1[left] != s1[right]:
                return False
            left += 1 
            right -= 1 
        return True
