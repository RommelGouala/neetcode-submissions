class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myFreq = {}

        for i,d in enumerate(nums):
            complement = target - d

            if complement in myFreq:
                return [myFreq[complement], i]
            else:
                myFreq[d] = i