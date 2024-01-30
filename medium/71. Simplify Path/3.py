class Solution:
    def simplifyPath(self, path):
        dir = []
        path = path.split('/')

        for elem in path:
            # 이전 파일로 가는거면
            if dir and elem == "..":
                dir.pop()
            # 나머지 경우 추가
            elif elem not in ["", ".", ".."]:
                dir.append(elem)
        
        return "/" + "/".join(dir)