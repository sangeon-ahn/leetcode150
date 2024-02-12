class Solution:
    @functools.lru_cache(maxsize=1000)
    def minDistance(self, word1, word2):
        if not word1 and not word2:
            return 0
        if not word2:
            return len(word1)
        if not word1:
            return len(word2)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        
        inserted = 1 + self.minDistance(word1, word2[1:])
        deleted = 1 + self.minDistance(word1[1:], word2)
        replaced = 1 + self.minDistance(word1[1:], word2[1:])

        return min(inserted, deleted, replaced)

sol = Solution()
ans = sol.minDistance("horse", "ros")
print(ans)