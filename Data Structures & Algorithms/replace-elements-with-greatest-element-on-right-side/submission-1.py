class Solution:
    
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i, num in enumerate(arr):
            largest_right = -1
            for j in range(i + 1, len(arr)):
                largest_right = max(largest_right, arr[j])
            arr[i] = largest_right
        arr[len(arr) - 1] = -1
        return arr