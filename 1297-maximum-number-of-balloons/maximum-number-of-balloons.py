class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count frequencies of the required characters
        b = text.count('b')
        a = text.count('a')
        l = text.count('l') // 2  # Requires 2 'l's per word
        o = text.count('o') // 2  # Requires 2 'o's per word
        n = text.count('n')

        # The bottleneck dictates the maximum instances possible
        return min(b, a, l, o, n)
