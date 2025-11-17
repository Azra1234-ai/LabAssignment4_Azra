def count_vowels_few(s):
    s = s.lower()
    vowels = "aeiou"
    return sum(1 for ch in s if ch in vowels)
# Example usage:
print(count_vowels_few("Hello World"))
print(count_vowels_few("abcdefghijklmnopqrstuvwxyz"))
