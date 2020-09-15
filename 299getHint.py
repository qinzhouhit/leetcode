'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List
from collections import Counter

class Solution:
    # official, two pass
    def getHint(self, secret: str, guess: str) -> str:
        h = Counter(secret)
            
        bulls = cows = 0
        for idx, ch in enumerate(guess):
            if ch in h:
                # corresponding characters match
                if ch == secret[idx]:
                    # update the bulls
                    bulls += 1
                    # update the cows 
                    # if all ch characters from secret 
                    # were used up
                    cows -= int(h[ch] <= 0)
                # corresponding characters don't match
                else:
                    # update the cows
                    cows += int(h[ch] > 0)
                # ch character was used
                h[ch] -= 1
                
        return "{}A{}B".format(bulls, cows)
        
    # self-made; T: O(N), S: O(1)
    # the trick is that you need to update the cow even when guessing correctly
    # e.g., s: 1122 and g: 1222, when guess the 2st 2, no 2 in s anymore, thus
    # you have to decrease cow by 1
    # sort of like A first, then B, e.g, 1122 and 2222 -> 2A0B
    def getHint1(self, secret: str, guess: str) -> str:
        cta = 0; ctb = 0
        hashmap = Counter(secret)
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                cta += 1
                if hashmap[guess[i]] > 0:
                    hashmap[guess[i]] -= 1
                else:
                    ctb -= 1
            if guess[i] != secret[i] and guess[i] in secret and hashmap[guess[i]]>0:
                ctb += 1
                hashmap[guess[i]] -= 1
            
        return f'{cta}A{ctb}B'