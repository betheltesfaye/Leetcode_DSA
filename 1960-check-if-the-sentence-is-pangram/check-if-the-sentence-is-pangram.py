class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # By converting the sentence to a set, we filter out all duplicate letters.
        # If the count of unique characters is 26, it contains every letter of the alphabet.
        return len(set(sentence)) == 26