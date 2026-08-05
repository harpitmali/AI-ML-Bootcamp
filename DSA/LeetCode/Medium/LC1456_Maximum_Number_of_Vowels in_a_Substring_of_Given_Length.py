def max_number_of_vowel(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    window_vowel = 0
    for i in range(k):
        if s[i] in vowels:
            window_vowel += 1
        
    max_vowel = window_vowel

    for i in range(k, len(s)):
        if s[i] in vowels:
            window_vowel += 1
        
        if s[i-k] in vowels:
            window_vowel -= 1

        max_vowel = max(max_vowel, window_vowel)

    return max_vowel

s = "leetcode"
k = 3

print(max_number_of_vowel(s, k))