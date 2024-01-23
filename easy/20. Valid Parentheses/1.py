from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        dic = defaultdict(str)
        dic[')'] = '('
        dic[']'] = '['
        dic['}'] = '{'

        for ch in s:
            if ch in ['[', '(', '{']:
                st.append(ch)
            else:
                # 스택 비어있으면 False
                if not st:
                    return False
                
                # 들어있는데 짝이 안맞으면 False
                if dic[ch] != st[-1]: 
                    return False
                
                # 짝 맞으면 pop
                st.pop()
        
        # 다 끝났는데 스택 안 비어있으면 false
        if st:
            return False
        return True
                
                

        