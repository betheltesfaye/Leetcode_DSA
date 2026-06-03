class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        final = []
        # Loop through indices from 0 to len(words) - 1
        for i in range(len(words)):
            # Access the word at the current index
            word = words[i]
            for char in word:
                if char == x:
                    final.append(i)
                    break
        return final