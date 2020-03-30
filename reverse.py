//https://leetcode.com/problems/reverse-integer/submissions/
class Solution:
    def reverse(self, x: int) -> int:
        if x > pow(2, 31) - 1 or x < pow(2, 31) * -1:
            return 0
        if x < 0:
            ret =  -1 * int(str(-1 * x)[::-1])
        else:
            ret = int(str(x)[::-1])
        if ret > pow(2, 31) - 1 or ret < pow(2, 31) * -1:
            return 0
        return ret
