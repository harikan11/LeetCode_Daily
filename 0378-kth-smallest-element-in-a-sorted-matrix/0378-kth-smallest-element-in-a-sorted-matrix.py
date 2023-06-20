class Solution:
    def countLessEqual(self, matrix, target):
        count = 0
        row = len(matrix) - 1
        col = 0
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] <= target:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count

    def kthSmallest(self, matrix, k):
        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right:
            mid = left + (right - left) // 2
            count = self.countLessEqual(matrix, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid

        return left

                    