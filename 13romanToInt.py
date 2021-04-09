'''
keys:
Solutions:
Similar:
T:
S:
'''


class Solution:
    # O(1) for S and T since worst case is limited
    def romanToInt(self, s):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        
        s2v={}
        for i in range(len(values)):
            s2v[numerals[i]] = values[i]

        sum_ = 0; i = 0
        while i < len(s):
            if i < len(s)-1 and s[i:i+2] in s2v: # two Roman chars
                sum_ += s2v[s[i:i+2]]
                i += 2
            else: # one char Roman char
                sum_ += s2v[s[i]]
                i += 1
        return sum_

    # else
    def romanToInt1(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]

obj=Solution()
print(obj.romanToInt("III"))



## Currency Rate Converter
# today_rate =  { ‘USDCAD’ = 1.1,      ‘USDEUR’ = 0.9}
# compute(today_rate, ‘USD’, 'CAD' )  ==> 1.1
# compute(today_rate, ‘CAD’, ‘USD’) 1/1.1
# compute(today_rate, ‘CAD’, ‘EUR’)  CADEUR = CADUSD * USDEUR = 1/1.1 * 0.9 | CAD -> USD -> EUR
# DFS
# BFS
'''
‘USDCAD’ = 1.1  
‘USDEUR’ = 0.9 => USD: [CAD: 1.1, EUR: 0.9], list of dictionary
today_rate_rev = defaultdict(dict)
today_rate_rev["USD"]["CAD"] = 1.1
for vals in today_rate_rev["CAD"]:
    
'''
def compute(self, today_rate, from_cur, to_cur): 





"""
  A             A
 / \            B C
B   C           F D E
|  / \          
F D   E         
"""
'''
tmp = []
[A] -> 1
[B, C] -> 2
[C, F...] -> 3 
res.append(tmp)
'''

class Node():
    val = None
    left = None
    right = None

    def __init__(self, val):
        self.val = val

from collections import deque
def levelTraversal(root):
    # output: level res string
    if not root:
        return "" # empty
    
    q = deque([root])
    res = []
    while q:
        cur_level = []
        len_cur_level = len(q)
        for _ in range(len_cur_level):
            node = q.popleft()
            cur_level.append(node.val) # "B C"
            if node.left: # non-None
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(cur_level)
    print(res)
    """
    [[A], [B, C], [F, D, E]]
    "A\n
    B C\n
    F D E\n"
    """
    str_res = ""
    for level in res: # level: list
        str_res += " ".join([str(x) for x in level])
        str_res += "\n" # str append
    return str_res # str 
    
"""
output:         input:
  A             A
 / \            B C
B   C           F * D E
|\ / \          G H * * I J K L
F*D   E         
"""
# input: multi-line string => [[1], [2,3], ...]
# root = Node(A)
# [A] -> root (q)
# [B, C] -> node A, A.left = B, A.right = C
# q: [B, C]
# [C, F]

