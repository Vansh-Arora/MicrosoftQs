def lis(A):
    maxi = 1
    n = len(A)
    for i in range(n-1):
        length = 1
        for j in range(i+1,n):
            if A[j] > A[i]:
                length += 1
        if length > maxi:
            maxi = length
    print(maxi)
    return maxi

A = [ 69, 54, 19, 51, 16, 54, 64, 89]
lis(A)