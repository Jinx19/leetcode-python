"""
153. 数字组合 II
样例
给出一个例子，候选数字集合为[10,1,6,7,2,1,5] 和目标数字 8  ,

解集为：[[1,7],[1,2,5],[2,6],[1,1,6]]

list[list[]] 重复问题
"""


class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum2(self, candidates, target):
        """write your code here"""
        result = list()
        path = list()
        candidates.sort()
        self.dfs(candidates, target, path, result)
        return result

    def dfs(self, candidates, target, path, result):
        if target < 0:
            return
        if target == 0:
            if path not in result:
                result.append(list(path))
            return
        m = len(candidates)
        for i in range(m):
            if i == 0 or (i > 0 and candidates[i] != candidates[i - 1]):
                path.append(candidates[i])
                self.dfs(candidates[i + 1:], target - candidates[i], path, result)
                path.remove(candidates[i])


# test
candidates = [7, 1, 2, 5, 1, 6, 10]
target = 8
solution = Solution()
print(solution.combinationSum2(candidates, target))
