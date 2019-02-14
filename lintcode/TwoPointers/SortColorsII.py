class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        def helper(colors,min,max,start,end):
            if max <= min:
                return
            lo,mid,hi = start,start,end
            while mid <= hi:
                if colors[mid] == min:
                    colors[lo],colors[mid] = colors[mid],colors[lo]
                    lo += 1
                    mid += 1
                elif colors[mid] == max:
                    colors[hi],colors[mid] = colors[mid],colors[hi]
                    hi -= 1
                else:
                    mid += 1
            helper(colors,min + 1,max - 1,lo,hi)

        helper(colors,1,k,0,len(colors) - 1)

s = Solution()
colors = list([3,2,2,1,4])
k = 4
s.sortColors2(colors,k)
print(colors)