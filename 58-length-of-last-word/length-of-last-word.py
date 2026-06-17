class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordStr = ""
        word = []
        wordsList = []
        finalList = []
        for i in s:
            word.append(i)
        for i in word:
            if i != " ":
                wordStr += i
            else:
                wordsList.append(wordStr)
                wordStr = "" 
        
        wordsList.append(wordStr)

        for i in wordsList:
            if i != "":
                finalList.append(i)
            else:
                continue
        
        # print(wordsList[0] == "")

        print(finalList)

        return len(finalList[-1])

        
