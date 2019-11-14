class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        max_len = float('-inf')
        max_str = ""
        dp = [[0 for x in range(len(s))] for y in range(len(s))]
        
        # single characters which are always palindrome
        for i in range(len(s)):
            dp[i][i] = 1
            max_len = 1
            max_str = s[i]
        
        # two characters
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                max_len = 2
                max_str = s[i:i+2]
                
        # More than 2 characters
        k = 3
        while k <= len(s):
            i = 0
            while i + k - 1 < len(s):
                j = i + k - 1
                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                    if k > max_len:
                        max_len = k
                        max_str = s[i:i + k]
                i+=1
            k += 1
        
        return max_str