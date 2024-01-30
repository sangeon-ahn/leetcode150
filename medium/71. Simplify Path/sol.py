"""
    정말 간단한 솔루션.
    실제 폴더만 dir에 넣어주고, /는 마지막에 사이사이에 추가하는 방식으로 구현.
    -> / 중복체크할 필요 없음.
"""
class Solution:
    def simplifyPath(self, path):
        dir = []
        path = path.split("/")

        for elem in path:
            if dir and elem == "..":
                dir.pop()
            elif elem not in [".", "", ".."]:
                dir.append(elem)
        
        return "/" + "/".join(dir)