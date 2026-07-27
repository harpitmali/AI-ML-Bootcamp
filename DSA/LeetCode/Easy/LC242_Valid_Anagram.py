"""def is_anagram(str1, str2):
    freq1 = frequency_counter(str1)
    freq2 = frequency_counter(str2)

    return freq1 == freq2
    
def frequency_counter(text):
    frequency_dict = {}

    for ch in text:
        if ch in frequency_dict:
            frequency_dict[ch] += 1
        else:
            frequency_dict[ch] = 1

    return frequency_dict

s = "anagram"
t = "nagaram"

print(is_anagram(s,t))"""


# Better optimization 

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    freq = {}

    for ch in str1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in str2:
        if ch not in freq:
            return False
        
        freq[ch] -= 1

        if freq[ch] < 0:
            return False
    
    return True

s = "anagram"
t = "nagaram"

print(is_anagram(s,t))