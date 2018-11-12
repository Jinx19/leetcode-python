class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        """write your code here"""
        result = list()
        path = list()
        self.dfs(candidates, target, path, result)
        return result

    def dfs(self, candidates, target, path, result):
        if target < 0:
            return
        if target == 0:
            path.sort()
            result.append(list(path))
            return
        m = len(candidates)
        for i in range(m):
            if i == 0 or (i > 0 and candidates[i] != candidates[i - 1]):
                path.append(candidates[i])
                self.dfs(candidates[i:], target - candidates[i], path, result)
                path.remove(candidates[i])
