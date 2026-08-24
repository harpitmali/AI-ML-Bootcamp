def longest_k_distinct(s, k):
    left = 0
    answer = 0
    freq = {}
    
    for right in range(len(s)):
        char = s[right]
        freq[char] = freq.get(char, 0) + 1

        while len(freq) > k:
            left_char = s[left]

            freq[left_char] -= 1
            
            if freq[left_char] == 0:
                del freq[left_char]

            left += 1

        answer = max(answer, right - left + 1)

    return answer


s = "eceba"
k = 2

print(longest_k_distinct(s, k))