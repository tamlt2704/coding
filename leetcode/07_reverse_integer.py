class Solution:
    def reverse(self, x: int) -> int:
        sign, x = (1, x) if x > 0 else (-1, -x)
        x = int(str(x)[::-1])
        
        return 0 if x > (2**31 -1) else sign * x
