class Solution:
    def reverseBits(self, n: int) -> int:
        
        binary = bin(n)[2:]
        count = 32 - len(binary)
        binary = binary[::-1]
        for i in range(count):
            binary += '0'
        return int(binary, 2)