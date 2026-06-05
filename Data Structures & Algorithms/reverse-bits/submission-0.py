class Solution:
    def reverseBits(self, n: int) -> int:
        bits = format(n, '032b')
        reversed_bits = bits[::-1]
        n = int(reversed_bits, 2)
        return n