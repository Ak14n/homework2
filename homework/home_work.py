def palindrome(word):
    word = word.lower()
    return word == word[::-1]
word = input("Введите слово: ")
result = palindrome(word)
if result:
    print("true")
else:
    print("false")