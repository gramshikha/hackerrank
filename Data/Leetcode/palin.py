import re
"""
A phrase is a palindrome if,
after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

def ispalindrome(a):
    
	# return True if a == a[::-1] else False
	mylist = []
	a = a.lower()
	print(a)
	a = re.sub(r'[^a-zA-Z0-9]', '', a)
	print(a)
	for x in a:
		mylist.append(x)

	if mylist[-1] == mylist[0]:
		# print("Palindrome")
		result = True
	else:
		# print("not Palindrome")
		result = False

	return result
		 

print(ispalindrome("A man, a plan, a canal: Panama"))