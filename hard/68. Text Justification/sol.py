from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line = [] # 단어가 추가됨.
        lineLen = 0 # 단어 길이만 추가됨.

        for word in words:
            # 단어 더했는데 초과하면(lineLen: 단어길이의 합, len(word): 다음 단어 길이, len(line): 단어 사이의 공백들 개수)
            if lineLen + len(word) + len(line) > maxWidth:
                # 추가되어야 할 공백길이 구하고,
                spaces = maxWidth - lineLen

                for i in range(spaces):
                    line[i % (len(line) - 1) or 1] += ' '
                
                lines.append(''.join(line))

                line = []
                lineLen = 0

            line.append(word)
            lineLen += len(word)
        
        lastLine = ''.join(line)
        lastLine += ' ' * (maxWidth - len(lastLine))
        lines.append(lastLine)

        return lines
