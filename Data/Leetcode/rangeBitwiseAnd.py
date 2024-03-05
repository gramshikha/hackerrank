class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        l = []
        for i in range(left,right+1):
           l.append(bin(i))
        
        print(l)

        r = int(l[0], 2)
        for i in l:
            r &= int(i, 2)

        print(r)
        return True




sol = Solution()

print(sol.rangeBitwiseAnd(5, 7))
        


"""
Optimal solution:

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        return left << shift

# Example usage:
sol = Solution()
result = sol.rangeBitwiseAnd(5, 7)
print(result)

"""
