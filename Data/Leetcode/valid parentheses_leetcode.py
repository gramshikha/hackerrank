#Best Solution
class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
    


    
sol = Solution()
bracket = "()[]"
print(sol.isValid(bracket))


#My solution
'''
class Solution:
    def isValid(s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    rev = stack[-1]
                    if (i == ']' and rev == '[') or (i == ')' and rev == '(') or (i == '}' and rev == '{'):
                        stack.pop()
                    else:
                        #print("false")
                        return False
        if not stack:
            return True
        else:
            return False
    
    bracket = "()["
    print(isValid(bracket))
    '''
    
                        
                