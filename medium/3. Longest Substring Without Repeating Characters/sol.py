class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = 0
        ans = 0
        seen = {}

        for idx, letter in enumerate(s):
            # letter이 이미 존재하면 해당 위치 + 1로 시작위치를 이동
            if seen.get(letter, -1) >= st: 
                st = seen[letter] + 1
            
            ans = max(ans, idx - st + 1)  # st ~ idx까지 길이
            seen[letter] = idx # 해당 문자 시작위치 갱신
        
        return ans

