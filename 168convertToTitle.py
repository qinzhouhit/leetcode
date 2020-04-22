'''
keys: //: (floor) integer divisor, %: remainder
Solutions:
Similar:
T: O(log_26 n)
S:
'''
import string

class Solution:
    # mine version, O(log_26 n)
    # An improve could be that only use list which has a O(1) complexity appending,
    # and only concatenate once at the end. The time complexity will be O(n),
    # but the code need more lines.
    def convertToTitle(self, n: int) -> str:
        import string
        if n <= 0:
            return ""
        res = [] # use list instead of string concatenation
        while n > 0:
            res.append(string.ascii_uppercase[(n-1)%26])
            n = (n-1)//26
        return "".join(res[::-1])


    # ord: return an integer representing the Unicode character.
    # The chr() method returns a character (a string) from an integer
    # recursive, O((n/26)^2)
    def convertToTitle(self, n):
        return "" if n == 0 \
            else self.convertToTitle((n - 1) / 26) + chr((n - 1) % 26 + ord('A'))


    def convertToTitle1(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26 #
        result.reverse()
        return ''.join(result)

    def convertToTitle2(self, n):
        result = ''
        distance = ord('A')

        while n > 0:
            y = (n-1) % 26
            n = (n-1) // 26
            s = chr(y+distance)
            result = ''.join((s, result))
        return result

    def convertToTitle4(x):
        result = []
        while x > 0:
            result.append(string.ascii_uppercase[(x - 1) % 26])
            x = (x - 1) // 26
        return "".join(reversed(result))

