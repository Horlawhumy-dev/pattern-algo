

def fruits_into_baskets(arr: list) -> list:
    """
        Time Complexity: O(n)
        Space Complexity: O(n)
        params:
            arr: list of fruits trees in the fruits list
        returns: length of 2 distinct fruit three in the array
    """
    window_start = 0
    max_length = 0
    char_freq = {}
    
    if len(arr) <= 0:
        return 0
    
    if len(arr) == 1:
        return 1
    
    for window_end in range(len(arr)):
        forward_char = arr[window_end]
        
        if forward_char not in char_freq:
            char_freq[forward_char] = 1
        else:
            char_freq[forward_char] += 1
            
            
        while len(char_freq) > 2:
            backward_char = arr[window_start]
            char_freq[backward_char] -= 1
            
            if char_freq[backward_char] == 0:
                del char_freq[backward_char]
                
            window_start += 1
            
        max_length = max(max_length, window_end-window_start+1)
    return max_length


arr = ["A", "B", "B", "C", "B", "B"]
print(fruits_into_baskets(arr))