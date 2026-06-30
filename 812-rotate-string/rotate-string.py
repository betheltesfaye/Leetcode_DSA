class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        truthValue = True
        for i in s:
            if s != goal:
                s = s[1:] + s[0]
                print(s)
            else:
                return True

        return False