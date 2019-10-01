class TwoSum:
    def __init__(self):
        self.nums = {}

    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        nums = self.nums
        for number in nums:
            if value - number == number:
                if nums[number] > 1:
                    return True
            elif value - number in nums:
                return True
        return False


s = TwoSum()
s.add(2)
s.add(3)
re = s.find(4)
print(re)
re = s.find(5)
print(re)
re = s.find(6)
print(re)
s.add(3)
re = s.find(6)
print(re)
