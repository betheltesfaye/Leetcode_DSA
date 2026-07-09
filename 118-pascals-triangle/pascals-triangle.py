class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        triangle = [[1]]
        
        for i in range(1, numRows):
            prev_row = triangle[-1]
            # Start each row with 1
            current_row = [1]
            
            # Each interior element is the sum of the two elements above it
            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])
            
            # End each row with 1
            current_row.append(1)
            triangle.append(current_row)
            
        return triangle

        #