#Best solution
class Solution:
    def lengthOfLastWord(s: str) -> int:
        # li = s.strip().split()
        print((s.strip().split()[-1]))
        return len(s.strip().split()[-1])

    #get_str = input("Enter your string: ")
    #if 1 <= len(get_str) <= 10 ** 4:
    print(lengthOfLastWord("Enter your string    "))

#My solution

'''
class Solution:
    def lengthOfLastWord(s: str) -> int:
        
        rev = s[::-1]
        my_str_list = rev.split(" ")
        
        print(my_str_list)
        count = 0
        for inte in my_str_list:
            if count == 0:
                if inte == " ":
                    pass
                else:
                    count = len(inte)
                

        return count

    get_str = input("Enter your string: ")
    #if 1 <= len(get_str) <= 10 ** 4:
    print(lengthOfLastWord(get_str))
    '''