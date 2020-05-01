Hamming weight:
   Count the number of ones by logical and of num and num-1
   class Solution:
    def hammingWeight(self, n: int) -> int:
        data = {1:1,2:1,3:2,4:1,5:2,6:2,7:3,8:1,9:2}
        num_one = 0
        if n <=0:
            return 0
        while (n):
            num_one += 1
            n &= n - 1
        return num_one

Hamming distance:
   difference between number of bits set beween two number
   find xor and count the number of 1s
       def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        count = 0
        print(x,y,diff)
        while diff:
            count +=1
            diff = diff & (diff-1)
        return count
