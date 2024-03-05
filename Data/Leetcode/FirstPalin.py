"""
Given an array of strings words, return the first palindromic string in the array.
If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward.

Example 1:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
"""

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        pal = []
        for i in words:
            if i == i[::-1]:
                pal.append(i)
        p = ""
        if len(pal) != 0:
            p = pal[0]
        
        return p



sol = Solution()
example = ["abc","car","ada","racecar","cool"]
print(sol.firstPalindrome(example))



"""
optimised sol:

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word[::-1] == word:
                return word
        return ""
        
"""