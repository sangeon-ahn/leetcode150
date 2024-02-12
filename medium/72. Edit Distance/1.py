class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        st = []
        ans = float('inf')

        def recur(idx1, idx2, cnts):
            nonlocal ans, st

            if idx2 == len(word2):
                if ''.join(st) == word2:
                    ans = min(ans, cnts + len(word1) - idx1)
                return
            
            for i in range(idx1, len(word1)):
                # 경우의 수: 무시하기, 집어넣기, 삭제하기, 교체하기, 삽입하기 -> 5개
                for j in range(5):
                    # 무시하기
                    if j == 0:
                        recur(i + 1, idx2, cnts)
                    # 집어넣기
                    elif j == 1:
                        st.append(word1[i])
                        recur(i + 1, idx2 + 1, cnts + 1)
                        st.pop()
                    # 삭제하기
                    elif j == 2:
                        recur(i + 1, idx2, cnts + 1)
                    # 교체하기
                    elif j == 3:
                        st.append(word2[idx2])
                        recur(i + 1, idx2 + 1, cnts + 1)
                    # 삽입하기
                    else:
                        st.append(word2[idx2])
                        recur(i, idx2 + 1, cnts + 1)
                        st.pop()
        recur(0, 0, 0)
        return ans

sol = Solution()
ans = sol.minDistance("horse", "ros")
print(ans)