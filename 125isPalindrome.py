'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # T: O(n); S: O(1)
    # The isalnum() method returns True if all characters in the string are 
    # alphanumeric (either alphabets or numbers). If not, it returns False.
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else: # l and r are number or char
                if s[l].lower() != s[r].lower(): # .lower() no error on digit str
                    return False
                else:
                    l += 1
                    r -= 1
        return True

obj = Solution()
obj.isPalindrome("A man, a plan, a canal: Panama")

