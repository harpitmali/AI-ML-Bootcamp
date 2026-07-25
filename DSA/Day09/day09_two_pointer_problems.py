def reverse_vowels(words):
    left = 0
    right = len(words)-1
    chars = list(words)

    while left <= right:
        if chars[left] in "aeiou" and chars[right] in "aeiou":
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        elif chars[left] not in "aeiou" and chars[right] in "aeiou":
            left += 1
        elif chars[left] in "aeiou" and chars[right] not in "aeiou":
            right -= 1
        else:
            left += 1
            right -= 1
    
    result = "".join(chars)
    return result

words = "leetcode"
print(reverse_vowels(words))