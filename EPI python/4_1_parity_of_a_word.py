'''
Parity of a word is 1 if the number of 1's in the word is odd.
Otherwise it is 0.
parity of 1011 is 1
parity of 10001000 is 0

Algo: Bruteforce
1.Test each bit while keeping track of the number of 1's seen so far.
'''
#bruteforce
def parity(x):
    res = 0
    while x:
        res ^= x & 1
        x >>= 1
    return res
if __name__ == "__main__":
    test=parity(1101)
    print (test)