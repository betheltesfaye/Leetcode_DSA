class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highestAlt = [0]
        for i in range(0, len(gain)):
            highestAlt.append(highestAlt[i] + gain[i])

        return max(highestAlt)
        

