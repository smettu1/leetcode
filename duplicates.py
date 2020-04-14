# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dup = 0
        for i in range(len(nums)):
            if i ==0:
                number = nums[i]
            else:
                if nums[i] == number:
                    nums[i] = None
                    dup +=1
                else:
                    number = nums[i]
        for i in range(dup):
            nums.remove(None)
        return len(nums)
