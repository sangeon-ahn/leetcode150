class MinStack:
    
    def __init__(self):
        self.st = [(float('inf'), float('inf'))]
        
    def push(self, val: int) -> None:
        self.st.append((val, min(val, self.st[-1][1])))
        
    def pop(self) -> None:
        self.st.pop()
        
    def top(self) -> int:
        return self.st[-1][0]
        

    def getMin(self) -> int:
        return self.st[-1][1]

        


# # # Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# query = ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
# vals = [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
# # output = [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483646,null,-2147483648,-2147483648,null,2147483646]
# # expected = [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647,null,-2147483648,-2147483648,null,2147483647]
# for i in range(len(query)):
#     if query[i] == "MinStack":
#         if not obj.st:
#             print("null")
#         else:
#             print(obj.st[-1][1])
#     elif query[i] == "push":
#         print("null")
#         obj.push(vals[i][0])
#     elif query[i] == "top":
#         print(obj.top())
#     elif query[i] == "getMin":
#         print(obj.getMin())
#     elif query[i] == "pop":
#         print("null")
#         obj.pop()
# # obj.push(val)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()
