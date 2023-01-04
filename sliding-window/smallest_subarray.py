
import math

def smallest_subarray(arr: list(), S: int) -> int:
    """
        Time Complexity: O(n)
        Space Complexity: O(1)
        params:
            arr: list of integers e.g [1, 3, 2, 6, -1, 4, 1, 8, 2]
            S: int sum of smallest subarray
        returns: length smallest subarray that sum is greater than or equals to S
    """
    window_start, window_sum = 0, 0
    window_min_length = math.inf
    
    if S <= 0 or len(arr) == 0:
        return 0
    

    for window_end in range(len(arr)):
        
        window_sum += arr[window_end]
        
        while window_sum >= S:
            window_min_length = min(window_min_length, (window_end - window_start + 1))
            window_sum -= arr[window_start]
            window_start += 1
            
    if window_min_length == math.inf:
        return 0
    
    return window_min_length

    
arr = [-2,1,-3,4,-1,2,1,-5,4]
smallest_subarr = smallest_subarray(arr, 6)
print(smallest_subarr)