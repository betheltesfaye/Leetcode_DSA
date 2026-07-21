class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        allX = s.count(x) * x
        allY = s.count(y) * y
        newStr = allY + allX
        # newStr.append(allY)
        # newStr.append(allX)

        print(allX)
        print(allY)

        print(newStr)

        for i in s:
            if (i == x) or (i == y):
                continue
            else:
                newStr += i

        return newStr
