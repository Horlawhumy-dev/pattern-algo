

def max_sum_subarray_of_size_k(arr: list(), k: int) -> int:
    """
        Time Complexity: O(n)
        Space Complexity: O(1)
        params:
            arr: list of integers e.g [1, 3, 2, 6, -1, 4, 1, 8, 2]
            k: int size
        returns: maximum sum of subarray of size k
    """
    window_start, window_sum = 0, 0
    max_sum = 0
    
    for i in range(len(arr)):
        
        window_sum += arr[i]
        
        #first calculate size of k before sliding the window
        if i >= k-1:
            max_sum = max(window_sum, max_sum)
            # removing the first element of each window
            window_sum -= arr[window_start]
            window_start += 1
            
    return max_sum
    
arr = [-2,1,-3,4,-1,2,1,-5,4]
max_sum_subarray = max_sum_subarray_of_size_k(arr, 4)
print(max_sum_subarray)