'''
__init__:
TC:
SC:

sumRegion:
TC:
SC:

Approach 1:
- We can calculate prefix sums row-wise per element
- Then for each row in the region, appropriately get each row sum and add
- TC(sumRegion): O(row2 - row1)

Approach 2:
- There is probably a way of making the TC(sumRegion): O(1)
- Let's calculate the prefix sum for each row (one per row, accumulates across rows)
- Let's calculate the prefix sum per element, column-wise (as we will not be selecting entire columns)
- Let's get the sum of the total array
- Then lets subtract the top, bottom, right and left area of the region from that total
- Didn't work, as e.g. compute left and right, is basically doing a variant of the problem (recursive)


Approach 3:
- Compute the prefix sum based on the top left, fusing row + top, so we have prefix sums for any quadrilateral originating from the origin


Constraints:
- There will at be one number in the matrix
- sumRegion will only be provided valid indices
- first coordinate always to the left of right coordinate
- matrix is either square or rectangular (quadrilateral)
'''

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        row_count, col_count = len(matrix), len(matrix[0])

        self.quad_prefix_sum = [[0] * (col_count + 1) for _ in range(row_count + 1) ]

        for r in range(row_count):
            row_prefix_sum = 0  
            for c in range(col_count):
                row_prefix_sum += matrix[r][c]
                above_quad_prefix_sum = self.quad_prefix_sum[r][c + 1]
                self.quad_prefix_sum[r + 1][c + 1] = (
                    row_prefix_sum
                    + above_quad_prefix_sum
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom_right = self.quad_prefix_sum[row2 + 1][col2 + 1]

        top = self.quad_prefix_sum[row1][col2 + 1]

        left = self.quad_prefix_sum[row2+1][col1]

        top_left = self.quad_prefix_sum[row1][col1]

        return (
            bottom_right
            - top
            - left
            + top_left
        )
        


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)