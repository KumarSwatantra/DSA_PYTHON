class Solution:
    def threeWayPartition(self, arr, a, b):
        start = 0
        end = len(arr) - 1
        i = 0

        while i <= end:
            if arr[i] < a:
                arr[i], arr[start] = arr[start], arr[i]
                start += 1
                i += 1

            elif arr[i] > b:
                arr[i], arr[end] = arr[end], arr[i]
                end -= 1

            else:
                i += 1

        return arr
