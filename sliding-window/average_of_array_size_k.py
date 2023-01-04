

def find_avg_of_array_size_k(arr: list(), k: int) -> list:
    """
        Time Complexity: O(n)
        Space Complexity: O(k)
        params:
            arr: list of integers e.g [1, 3, 2, 6, -1, 4, 1, 8, 2]
            k: int size
        returns: list of averages
    """
    result = []
    window_start= 0
    window_sum = 0
    
    for i in range(len(arr)):
        
        window_sum += arr[i]
        
        #first calculate size of k before sliding the window
        if i >= k -1:
            avg = window_sum / 5
            result.append(avg)
            
            # removing the first element of each window
            window_sum -= arr[window_start]
            window_start += 1
            
    return result
    
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
avg_array_of_size_k = find_avg_of_array_size_k(arr, 5)
print(avg_array_of_size_k)