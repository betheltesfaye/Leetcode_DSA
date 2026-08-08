class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternList = []
        sWord = ""
        sWordList = []
        for i in pattern:
            patternList.append(i)

        for i in s:
            if i == " ":
                sWordList.append(sWord)
                sWord = ""
            else:
                sWord += i
        
        sWordList.append(sWord)
        
        # print(patternList)
        # print(sWordList)


        
        if len(patternList) != len(sWordList):
            return False  # Length mismatch

        map1, map2 = {}, {}

        for i, j in zip(patternList, sWordList):
            # Check if item1's mapping conflicts
            if i in map1 and map1[i] != j:
                return False
            # Check if item2's mapping conflicts
            if j in map2 and map2[j] != i:
                return False

            map1[i] = j
            map2[j] = i

        return True  # No mismatch, patterns match perfectly


            