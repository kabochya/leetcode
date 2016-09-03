class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.bt = [0]*m*n
        self.M = m
        return self.path(m,n)
    def path(self,m,n):
        if m>1 and n>1:
            b = self.bt[self.M*(n-1)+m-1]
            if not b:
                b = self.bt[self.M*(n-1)+m-1]=self.path(m-1,n)+self.path(m,n-1)
            return b
        else:
            return 1
