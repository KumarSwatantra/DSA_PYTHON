class Solution:
    def rotate(self, arr, n):
        if n == 0:
            return arr
        
        last = arr[-1]

        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]

        arr[0] = last
        
        return arr
