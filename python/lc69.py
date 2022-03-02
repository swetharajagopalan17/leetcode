class Solution:
    def mySqrt(self, x: int) -> int:
        if x in (0, 1):
            return x
        
        l = 0
        r = x
        m = (l + r) // 2
        
        while l < m and m < r:
            p = m * m

            if p < x:
                l = m
            elif p > x:
                r = m
            else:
                break

            m = (l + r) // 2            
    
        return m
