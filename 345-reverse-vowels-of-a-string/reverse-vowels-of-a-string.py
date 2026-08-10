class Solution:
    def reverseVowels(self, s: str) -> str:
        sCons = []
        sVowels = []
        sVowelsRev = []
        count = 0
        sFinal = []
        for i in s:
            if (i == 'a' or i == 'A') or (i == 'e' or i == 'E') or (i == 'i' or i == 'I') or (i == 'o' or i == 'O') or (i == 'u' or i == 'U'):
                sVowels.append(i)
            else:
                sCons.append(i)

        
        sVowelsRev[:] = sVowels[::-1]

        print(sVowels)
        print(sVowelsRev)
        print(sCons)

        for i in range(len(s)):
            if (s[i] == 'a' or s[i] == 'A') or (s[i] == 'e' or s[i] == 'E') or (s[i] == 'i' or s[i] == 'I') or (s[i] == 'o' or s[i] == 'O') or (s[i] == 'u' or s[i] == 'U'):
                s = s[:i] + str(sVowelsRev[count]) + s[i + 1:]
                count += 1
            

        
        return s

