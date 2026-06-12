class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        maxUp = num
        maxDown = num
        x = 0
        for i in range(t):
            maxUp += 1
            maxDown -= 1
        
        if (maxUp == (num + t)):
            return (maxUp + t)
        # elif (maxDown == (num - t)):
        #     return maxDown - 1
            
        
        print(f"Num: {num}, MaxUp: {maxUp}, MaxDown: {maxDown}")
            