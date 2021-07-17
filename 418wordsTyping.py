""" 
keys: 
Solutions:
Similar:
T:
S:
"""


class Solution:
	# https://leetcode.com/problems/sentence-screen-fitting/discuss/90845/21ms-18-lines-Java-solution
	# explaination: 
	# https://leetcode.com/problems/sentence-screen-fitting/discuss/90845/21ms-18-lines-Java-solution/95272
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
    	# we need the space between words, the last blank is for next sentence
    	s = " ".join(sentence) + " "
    	start = 0  # index of pointer on concatenated sentences
    	l = len(s)
    	for i in range(rows):
    		start += cols  # for each row, filled
    		if s[start % l] == " ":
    			start += 1  # the piece can fit in row perfectly
    		else:
    			while start > 0 and s[(start-1) % l] != " ":
    				# retreat the pointer to the beginning of the word, 
    				start -= 1  # because a word cannot be split into two lines.
    	return start // len(s) 