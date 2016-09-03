class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        maps = {}
        for i in range(len(nums)):
            maps[nums[i]] = [i]+maps.get(nums[i],[])
        for i in maps:
            a = maps[i]
            if target==i*2:
                if len(a)==2:
                    return a
            else:
                b = maps.get(target-i)
                if b:
                    return [a[0],b[0]]
