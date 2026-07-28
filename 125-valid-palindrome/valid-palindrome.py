class Solution:
    def isPalindrome(self, s: str) -> bool:
        checkPal = ''
        checkPalRev = ''
        for i in s:
            if i.isalnum():
                checkPal += i
            else:
                continue

        for i in range(len(checkPal) - 1, -1, -1):
            checkPalRev += checkPal[i]

        print(checkPal)
        print(checkPalRev)

        return checkPal.casefold() == checkPalRev.casefold()
