class Solution:
    def minJumps(self, arr, n):
        if n <= 1:
            return 0

        maxReach = arr[0]
        steps = arr[0]
        jumpCount = 1

        for i in range(1, n):
            if i == n - 1:
                return jumpCount

            maxReach = max(maxReach, i + arr[i])
            steps -= 1

            if steps == 0:
                jumpCount += 1
                steps = maxReach - i

        return jumpCount
