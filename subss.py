max1 = 100000
mod = 1000000007
 
inv = [0 for i in range(max1)]
fact = [0 for i in range(max1)]
facinv = [0 for i in range(max1)]
 
# Function to precompute factorial and
# the inverse of factorial values of all
# elements in the range [1, max] to find
# the value of nCr in O(1)
def ncrPrecomputation():
    inv[0] = inv[1] = 1
    fact[0] = fact[1] = 1
    facinv[0] = facinv[1] = 1
 
    # Loop to iterate over all i in
    # the range [2, max]
    for i in range(2,max1,1):
        # Calculate Inverse of i
        inv[i] = inv[mod % i] * (mod - mod // i) % mod
 
        # Calculate Factorial of i
        fact[i] = (fact[i - 1] * i) % mod
 
        # Calculate the Inverse of
        # factorial of i
        facinv[i] = (inv[i] * facinv[i - 1]) % mod
 
# Function to find nCr in O(1)
def nCr(n,r):
    return ((fact[n] * facinv[r]) % mod * facinv[n - r]) % mod
 
# Function to find the sum of difference
# between maximum and minimum over all
# sets of arr[] having K elements
def sumMaxMin(arr, N, K):
    # Sort the given array
    arr.sort()
 
    # Stores the sum of maximum of
    # all the sets
    sumMax = 0
 
    # Loop to iterate arr[] in the
    # range [K-1, N-1]
    for i in range(K - 1,N,1):
        # Add sum of sets having arr[i]
        # as the maximum element
        sumMax += (arr[i] * nCr(i, K - 1))
 
    # Stores the sum of the minimum of
    # all the sets
    sumMin = 0
 
    # Loop to iterate arr[] in the
    # range [0, N - K]
    for i in range(N - K+1):
        # Add sum of sets having arr[i]
        # as the minimum element
        sumMin += (arr[i] * nCr(N - i - 1, K - 1))
 
    # Return answer
    return (sumMax - sumMin)
 
# Driver Code
if __name__ == '__main__':
    arr = [1, 1, 3, 4]
    K = 2
    N = len(arr)
    ncrPrecomputation()
    print(sumMaxMin(arr, N, K))
     
    # This code is contributed by SURENDRA_GANGWAR
