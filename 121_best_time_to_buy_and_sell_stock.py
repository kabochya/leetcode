class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret, min= 0, 999999
        for i in prices:
            if min>i:
                min = i
            elif i-min>ret:
                ret = i-min
        return ret
