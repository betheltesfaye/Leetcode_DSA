class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Check if right moves cancel left moves, and up moves cancel down moves.
        return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')