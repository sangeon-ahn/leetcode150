class Solution:
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)

        # dp[i][j]: word1은 i까지, word2는 j까지 볼 때 최저 변형횟수
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 해당 문자가 같은 경우,
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # 해당 문자가 다른 경우: 삽입(word2만 인덱스 증가), 삭제(word1만 인덱스 증가), 교체(word1, word2 둘다 인덱스 증가)
                else:
                    # (i, j)는 (i, j-1)에서 삽입했거나, (i-1, j)에서 삭제했거나, (i-1, j-1)에서 교체한 경우에 도달 가능
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        return dp[-1][-1]