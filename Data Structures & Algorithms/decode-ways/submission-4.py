class Solution:
    def numDecodings(self, s: str) -> int:
        # if starts with 1, second can be anything
        # if starts with 2, second can be 0-6
        # or it could be a single digit

        dp = {len(s):1}

        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
            print(i)
            if i+1<len(s) and (s[i] == '1' or (s[i] == '2' and int(s[i+1]) <= 6)):
                dp[i] += dp[i+2]
        
        return dp[0]
