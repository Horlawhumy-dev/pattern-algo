

def longest_substring_with_k_distinct(st: str, k: int) -> int:
    """
        Time Complexity: O(n)
        Space Complexity: O(n)
        params:
            st: str string of characters e.g "abracadabrra"
            k: int distinct size
        returns: length of longest substring with k distinct elements
    """
    window_start = 0
    max_length = 0
    char_freq = {}
    
    if len(st) <= 0 or k <= 0:
        return 0
    
    if len(st) == 1 or k == 1:
        return 1
    
    for window_end in range(len(st)):
        forward_char = st[window_end]
        
        if forward_char not in char_freq:
            char_freq[forward_char] = 1
        else:
            char_freq[forward_char] += 1
            
            
        while len(char_freq) > k:
            backward_char = st[window_start]
            char_freq[backward_char] -= 1
            
            if char_freq[backward_char] == 0:
                del char_freq[backward_char]
                
            window_start += 1
            
            max_length = max(max_length, window_start)
        print(char_freq)
    return max_length

st = "abcbbc"
print(longest_substring_with_k_distinct(st, 2))