class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int

        N = 2, K = 2

            0
        0       1
     0    1   1   0
    0  1 1 0 1 0 0  1





        """
        curr_digit = 0
        N = 2**(N-1)
        while N > 1:
            if K > N // 2: # second half
                K -= N // 2
                curr_digit = int(not curr_digit)
            N = N // 2


        return curr_digit
