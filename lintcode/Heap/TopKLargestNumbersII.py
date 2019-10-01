import heapq


class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.k = k
        self.q = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        # write your code here
        heapq.heappush(self.q, num)

    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        largetn = heapq.nlargest(self.k, self.q)
        print(largetn)


s = Solution(3)
s.add(3)
s.add(10)
s.topk()
s.add(1000)
s.add(-99)
s.topk()
s.add(4)
s.topk()
s.add(100)
s.topk()
