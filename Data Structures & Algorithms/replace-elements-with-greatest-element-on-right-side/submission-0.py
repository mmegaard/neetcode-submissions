class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest_right = arr[len(arr) - 1]
        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            arr[i] = largest_right
            largest_right = max(largest_right, current)
        arr[len(arr) - 1] = -1
        return arr