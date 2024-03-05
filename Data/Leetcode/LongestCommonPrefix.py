"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
Explanation: There is no common prefix among the input strings.
"""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        l = len(strs[0])
        p = []
        s = strs[0]
        m = []

        for i in strs:
            if len(i) < l:
                l = len(i)
                s = i

        for i in range(l):
            for j in strs:
                if j[i] != s[i]:
                    p.append(j[i])
            
            if len(p) == 0:
                m.append(j[i])

        m = "".join(m)

        return m

sol = Solution()
strs = ["dog","racecar","car"]
print(sol.longestCommonPrefix(strs))