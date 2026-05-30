class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for j in range(len(words)):
            for i in words:
                if [i] == [i[::-1]]:
                    return i
        
        return ""
