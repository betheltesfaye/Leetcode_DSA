class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        
        for word in words:
            # Calculate the total weight of the current word
            total_weight = sum(weights[ord(c) - ord('a')] for c in word)
            
            # Find the modulo 26 of the weight
            mod_val = total_weight % 26
            
            # Map to reverse alphabetical order: 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'
            mapped_char = chr(ord('z') - mod_val)
            
            result.append(mapped_char)
            
        return "".join(result)

        #needs to be reviewd