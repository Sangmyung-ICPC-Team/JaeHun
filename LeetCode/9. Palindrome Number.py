class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        pal_list = str(x)
        pal_rev_list = pal_list[::-1]
        return pal_list == pal_rev_list
