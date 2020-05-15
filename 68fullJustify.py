'''
keys: tricky for assign empty string
Solutions: https://www.youtube.com/watch?v=qrZLQmL6fyI&feature=youtu.be
Similar:
T:
S:
'''
from typing import List

class Solution:
    
    # intuitive version, many details
    def fullJustify1(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        ind = 0
        while ind < n:
            totalChars = len(words[ind]) # for this one line
            last = ind + 1 # move to next word, at least we can have one word for one line
            
            while last < n: # see how many words can be added for this line
                if totalChars + 1 + len(words[last]) > maxWidth: # one for the space
                    # between word ind and word next_
                    break # two words already longer than maxWidth
                totalChars += 1 + len(words[last])
                last += 1
            # last is actually the first index of the next line, so -1
            gaps = last - ind - 1 # gaps between words for one line
            cur_line = []
            
            if last == n or gaps == 0: # last word or no gaps
                for i in range(ind, last):
                    cur_line.append(words[i])
                    cur_line.append(" ")
                
                del cur_line[-1] # delete last blank space
                while len("".join(cur_line)) < maxWidth: # last line left just
                    cur_line.append(" ")
            else:
                spaces = (maxWidth - totalChars) // gaps # extra " " to add
                remainder = (maxWidth - totalChars) % gaps
                
                for i in range(ind, last - 1): # construct cur line
                    # ignore the last word since we don't need space after that
                    cur_line.append(words[i])
                    cur_line.append(" ")
                    end_ind = 1 if i-ind<remainder else 0 # extra " "
                    for j in range(spaces + end_ind): # insert extra " "
                        cur_line.append(" ")
                    
                cur_line.append(words[last-1]) # add the last word we ignored before
            res.append("".join(cur_line))
            ind = last # move to the next line
        return res
                
            
    
    # concise version
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur_line = []
        num_letters_line = 0
        for word in words:
            if num_letters_line + len(word) + len(cur_line) > maxWidth:
                for i in range(maxWidth - num_letters_line):
                    cur_line[i%(len(cur_line)-1 or 1)] += " "
                res.append("".join(cur_line))
                cur_line, num_letters_line = [], 0
            cur_line += [word]
            num_letters_line += len(word)
        return res + [" ".join(cur_line).ljust(maxWidth)]
                    
sol = Solution()
print (sol.fullJustify1(["This", "is", "an", "example", "of", "text", "justification."], 16))