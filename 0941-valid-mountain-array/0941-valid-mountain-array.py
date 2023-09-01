class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        strictly_increasing = strictly_decreasing = False

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                if strictly_decreasing:
                    return False
                strictly_increasing = True
            elif arr[i] < arr[i - 1]:
                if not strictly_increasing:
                    return False
                strictly_decreasing = True
            else:
                return False

        return True if strictly_increasing and strictly_decreasing else False