class Solution:
    def findComplement(self, num: int) -> int:
        # Get the number of bits required to represent num in binary
        bit_length = num.bit_length()
        
        # Create a bitmask of all 1s of the same length
        # Example for 5 (101): (1 << 3) - 1 = 8 - 1 = 7 (111)
        mask = (1 << bit_length) - 1
        
        # XOR the number with the mask to flip all bits
        return num ^ mask

        #