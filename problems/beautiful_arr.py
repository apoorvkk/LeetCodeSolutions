class Solution:
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        [....] [....]
        
            5
         /     \
      2         3
     / \     /    \
    1   1   1      2
                 /   \
                1    1
  [1,2]     [1, 2,4]
  
  [1, 3] [2,4,8]
        """
        dp = {}
        
        dp[1] = [1]
        
        for i in range(2, N+1):
            dp[i] = [x*2 for x in dp[i//2]] + [x*2-1 for x in dp[i-i//2]]
        return dp[N]