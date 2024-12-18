def is_palindrome(s):
    reversed_str = s[::-1]
    if s == reversed_str:
        return 1
    else:
        return 0

def palindrome(s):
    polindr = s
    suffix = ''
    word = ''
    if is_palindrome(polindr) == 1:
        return s
    for _ in range(len(s)):
        suffix = suffix + polindr[-1]
        polindr = polindr[:-1]
        word = suffix + s
        if is_palindrome(polindr) == 1:
            return word

word_input = input("Give a word:")
result_palindrome = palindrome(word_input)

print("The shortest palindrome is:", result_palindrome)



