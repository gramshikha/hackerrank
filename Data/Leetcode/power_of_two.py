"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false

Constraints:
-231 <= n <= 231 - 1
"""

class Solution:
    # c = 0
    # list1 = []
    
    def isPowerOfTwo(self, n: int) -> bool:

        c = 0
        if n == 1:
            return True
        
        elif n == 0 :
            return False
        
        else: 
            while n % 2 == 0:
                n //= 2
                if n % 2 == 0 or n == 1:
                    c += 1
                else:
                    c = 0

            return False if c == 0 else True



sol = Solution()

print(f"0: {sol.isPowerOfTwo(0)}")
print(f"1: {sol.isPowerOfTwo(1)}")
print(f"2: {sol.isPowerOfTwo(2)}")
print(f"4: {sol.isPowerOfTwo(4)}")
print(f"6: {sol.isPowerOfTwo(6)}")
print(f"8: {sol.isPowerOfTwo(8)}")
print(f"10: {sol.isPowerOfTwo(10)}")
print(f"12: {sol.isPowerOfTwo(12)}")
print(f"14: {sol.isPowerOfTwo(14)}")
print(f"16: {sol.isPowerOfTwo(16)}")
print(f"18: {sol.isPowerOfTwo(18)}")
print(f"20: {sol.isPowerOfTwo(20)}")


"""
Easy solution
--------
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
        
"""
