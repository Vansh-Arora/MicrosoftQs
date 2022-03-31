class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        n = len(A)
        count = 0
        ind = 0
        for i in range(n):
            if A[i] == A[ind]:
                count += 1
            elif count == 0:
                ind = i
                count += 1
            else:
                count -= 1
        if count > 0:
            return A[ind]