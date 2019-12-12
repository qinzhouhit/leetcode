class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        dp=[0]*(len(s)+1)
        dp[0]=1; dp[1]= 1 if s[0]!="0" else 0
        for i in range(2, len(s)+1):
            s1=int(s[i-1: i]); s2=int(s[i-2: i])
            if s1>=1 and s1<=9:
                dp[i]+=dp[i-1]
            if s2>=10 and s2<=26:
                dp[i]+=dp[i-2]
        return dp[-1]

obj=Solution()
print (obj.numDecodings("0"))




