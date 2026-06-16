class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize the first two steps
        two_steps_behind = 1  # W(1)
        one_step_behind = 2   # W(2)
        
        # Compute ways dynamically up to n
        for _ in range(3, n + 1):
            current_step = one_step_behind + two_steps_behind
            two_steps_behind = one_step_behind
            one_step_behind = current_step
            
        return one_step_behind
    
