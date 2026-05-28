class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        
        for sentence in sentences:
            # .split(' ') creates a list of words.
            # len() counts the number of elements in that list.
            word_count = len(sentence.split(' '))
            
            # Update max_words if the current sentence has more words.
            if word_count > max_words:
                max_words = word_count
                
        return max_words