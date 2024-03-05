#class Solution:
def isPalindrome(self, x) -> bool:
       # = x[::-1]
       y = x[::-1]
       
       if x == y:
           return True
       else:
           return False

print(isPalindrome("palindrome"))  