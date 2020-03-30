'''
Count the number of bits that are set to 1 in a positive integer.

Algo:
1.init a var to zero to hold the number of bits
2.while x is not zero go into the loop and check the bitwise AND operation of x and 1
3.Add the result of the AND operation to the var that is holding the number of bits.
4.right shift the number by 1 bit using bitwise right shift operator and continue the while loop
5.Return the number of bits.

Time complexity:
O(n)-->N being the number of bits in x and we check each bit.
'''

def count_bits(x):
    num_bits=0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

if __name__ == "__main__":
    i=count_bits(10)
    print(i)