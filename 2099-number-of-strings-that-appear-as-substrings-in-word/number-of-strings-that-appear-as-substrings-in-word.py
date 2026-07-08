class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for i in patterns:
            # Check if the pattern is a substring of word
            if i in word:
                count += 1
        return count


