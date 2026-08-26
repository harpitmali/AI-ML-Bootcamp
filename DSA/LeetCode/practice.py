def character_replacement(s, k):
    left = 0
    freq = {}
    max_freq = 0
    answer = 0

    for right in range(len(s)):

        freq[s[right]] = freq.get(s[right], 0) + 1

        max_freq = max(
            max_freq,
            freq[s[right]]
        )

        while (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1

            if freq[s[left]] == 0:
                del freq[s[left]]

            left += 1

        answer = max(
            answer,
            right - left + 1
        )

    return answer

s = "ABCDE"
k = 1

print(character_replacement(s, k))