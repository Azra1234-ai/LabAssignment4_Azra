def count_vowels_zero(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)


# Example usage:
print(count_vowels_zero("Hello World"))
print(count_vowels_zero("abcdefghijklmnopqrstuvwxyz"))
