"""
    <init>
    최소힙, 최대힙 생성
    
    <addNum>
    최소힙 비어있거나 둘이 크기 같으면 최소힙에 넣기
    최소힙이 더 크면 최대힙에 넣기

    이후 각 힙의 top 비교해서 최대힙 탑이 더 크면 양쪽 탑 교체

    <findMedian>
    두 힙 개수 짝수면 양쪽 힙에서 하나씩 뽑아 평균
    홀수면 최소힙에서 하나 뽑기
"""
import heapq
class MedianFinder:
    
    def __init__(self):
        self.hq1 = []
        self.hq2 = []

    def addNum(self, num: int) -> None:
        if not self.hq1 or len(self.hq1) == len(self.hq2):
            heapq.heappush(self.hq1, num)
        
        elif len(self.hq1) > len(self.hq2):
            heapq.heappush(self.hq2, -num)
        
        if not self.hq1 and not self.hq2 and self.hq1[0] < -self.hq2[0]:
            val1 = heapq.heappop(self.hq1)
            val2 = -heapq.heappop(self.hq2)

            heapq.heappush(self.hq1, val2)
            heapq.heappush(self.hq2, -val1)

    def findMedian(self) -> float:
        if (len(self.hq1) + len(self.hq2)) % 2 == 0:
            return (self.hq1[0] + self.hq2[0]) / 2 
        else:
            return self.hq1[0]
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()