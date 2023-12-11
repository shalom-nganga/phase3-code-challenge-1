def solve(s):
    vowels = "aeiou"
    consonant_values = {char: i + 1 for i, char in enumerate("abcdefghijklmnopqrstuvwxyz") if char not in vowels}

    current_consonant_value = 0
    highest_consonant_value = 0

    for char in s:
        if char not in vowels:
            current_consonant_value += consonant_values[char]
        else:
            highest_consonant_value = max(highest_consonant_value, current_consonant_value)
            current_consonant_value = 0

    # Check one more time in case the string ends with a consonant substring
    highest_consonant_value = max(highest_consonant_value, current_consonant_value)

    return highest_consonant_value

# Test cases
print(solve("zodiacs"))  # Output: 26
print(solve("strength"))  # Output: 57
