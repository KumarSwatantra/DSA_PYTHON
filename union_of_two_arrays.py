class Solution:
    def findUnion(self, a, n, b, m):
        union_set = set()

        for num in a:
            union_set.add(num)
        for num in b:
            union_set.add(num)

        result = sorted(list(union_set))
        return result
