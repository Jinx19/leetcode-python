import heapq

class Solution:
    def nthUglyNumber(self, n: 'int') -> 'int':
        q = [1,2,3,5]
        primes = [2,3,5]
        setq = {1,2,3,5}
        for i in range(n):
            number = heapq.heappop(q)
            for j in range(3):
                nextvalue = primes[j]*number
                if nextvalue not in setq:
                    heapq.heappush(q,nextvalue)
                    setq.add(nextvalue)
        return number

s = Solution()
# print(s.nthUglyNumber(1))
print(s.nthUglyNumber(7))

