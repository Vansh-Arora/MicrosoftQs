class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self,A):
        n = len(A)
        candies = [1 for i in range(n)]
        for i in range(1,n):
            if A[i] > A[i-1]:
                
                candies[i] = candies[i-1] + 1
        for i in range(n-2,-1,-1):
            if A[i] > A[i+1]:
                if candies[i] <= candies[i+1]:
                    candies[i] = candies[i+1] + 1
        sum = 0
        for i in candies:
            sum += i
        return sum