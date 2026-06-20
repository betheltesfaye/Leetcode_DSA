class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenNeedle = len(needle)
        for i in range(0, len(haystack)):
            if needle == haystack[i:lenNeedle]:
                return i
            else:
                lenNeedle += 1
        return -1

                