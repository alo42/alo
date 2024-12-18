def is_strong_password(password):
    def has_lowercase(s):
        return any('a' <= ch <= 'z' for ch in s)

    def has_uppercase(s):
        return any('A' <= ch <= 'Z' for ch in s)

    def has_digit(s):
        return any('0' <= ch <= '9' for ch in s)

    def has_special(s):
        special_characters = "~`!@#$%^&*()-_+={}[]|\\;:\"<>,./?"
        return any(ch in special_characters for ch in s)

    def has_repeating_characters(s):
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] == s[i + 2]:
                return True
        return False

    def has_consecutive_numbers(s):
        for i in range(len(s) - 1):
            if s[i].isdigit() and s[i + 1].isdigit() and abs(int(s[i]) - int(s[i + 1])) == 1:
                return True
        return False

    def has_sequential_characters(s):
        for i in range(len(s) - 2):
            if ord(s[i + 1]) - ord(s[i]) == 1 and ord(s[i + 2]) - ord(s[i + 1]) == 1:
                return True
        for i in range(len(s) - 1):
            if ord(s[i + 1]) - ord(s[i]) == 1:
                return True
        return False

    # Rules Check
    length = len(password)
    missing_types = 4 - sum([has_lowercase(password), has_uppercase(password), has_digit(password), has_special(password)])

    length_steps = 0
    if length < 8:
        length_steps = 8 - length
    elif length > 20:
        length_steps = length - 20

    repeating_steps = 0
    if has_repeating_characters(password):
        repeating_steps += 1

    consecutive_number_steps = 0
    if has_consecutive_numbers(password):
        consecutive_number_steps += 1

    sequential_steps = 0
    if has_sequential_characters(password):
        sequential_steps += 1

    # Calculate total steps
    total_steps = max(length_steps, missing_types) + repeating_steps + consecutive_number_steps + sequential_steps

    if total_steps == 0:
        return "good"
    return total_steps

# Example Usage
password = "aaE-d2c1"
result = is_strong_password(password)
print(result)









