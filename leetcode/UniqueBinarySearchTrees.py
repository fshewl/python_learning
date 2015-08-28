#
# https://leetcode.com/problems/unique-binary-search-trees/
#

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cache = {0: 1, 1: 1}
        return self.helper(n)
        
    def helper(self, n):
        # EAFP 
        try:
            # try to get from the cache
            num = self.cache[n]
        except KeyError:
            # generator expression
            num = sum(self.helper(i) * self.helper(n-i-1) for i in xrange(n))
                
            self.cache[n] = num
        
        return num
