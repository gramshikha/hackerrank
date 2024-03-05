class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        num_len = len(nums)
        list1 = []
        for i in range(0, num_len+1):
            list1.append(i)

        for lists in list1:
            if lists not in nums:
                return lists




sol = Solution()
num = [0,1,2,5,6,4]
print(sol.missingNumber(num))
